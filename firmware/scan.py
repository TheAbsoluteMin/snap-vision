from easygopigo3 import EasyGoPiGo3
from IPython.display import Image, display
from picamera2 import Picamera2
from picamera2 import libcamera
import cv2
import adafruit_dotstar as dotstar
import board
import time
import os
import requests
import zipfile
import urllib.parse
import subprocess
import shutil
import imaplib
import re
import email

### 0. Set up

#hardware
camera = Picamera2()
easyGPG = EasyGoPiGo3()
easyGPG.reset_encoders()
clock_pin = board.D6
data_pin = board.D5
num_leds = 120
brightness = 0.05
lights = dotstar.DotStar(clock_pin, data_pin, num_leds, brightness=brightness, auto_write=False)

##### Edit these! #####
token = "#####" #ask for a token at the official Open Scan API email: cloud@openscan.eu
IMAP = "imap.gmail.com" #fill out the below, optional but needed for 100% success to get downloadable link for 3D model
email_user = "#####" #your Gmail address
email_pass = "#####" #your Gmail app password

#API variables
folder = "/home/pi4/Camera/"
dir_temp = "/home/pi4/temp/"
zip_scanned = "/home/pi4/Scanned/"
zip_extracted = "/home/pi4/Extracted/"
server = "http://openscanfeedback.dnsuser.de:1334/"
user = "openscan"
pw = "free"
size_to_split = 200000000 #200MB max files size
msg = {"token": token}
allowed_extensions = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']

#get API requests
def OpenScanCloud(cmd, msg_req):
    return requests.get(server + cmd, auth=(user,pw), params=msg_req)

#clean all folders
folders_clean = ["/home/pi4/Camera/", "/home/pi4/temp/", "/home/pi4/Scanned/", "/home/pi4/Extracted/",]
for folder in folders_clean:
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder, exist_ok=True)

### 1. Scanning
#object preferences
object_name = input("Object Name: ")
num_photos = int(input("Number of Photos (20+ recommended): "))

#adaptive wheel speed
easyGPG.set_speed(10 * num_photos)
print(f"Speed: {10 * num_photos}.")

#LEDs on
lights.fill((255, 255, 255))
lights.show()
print("Lights on.")

#camera on max res: 4608 × 2592 pixels
cam_config = camera.create_still_configuration(main={"size": (4608, 2592)})
camera.configure(cam_config)
camera.set_controls(
    {
        "AwbMode": libcamera.controls.AwbModeEnum.Daylight,
        "AfMode": libcamera.controls.AfModeEnum.Manual, 
        "LensPosition": 12.0
    }
)
camera.start()
time.sleep(2)

cycle = 0
for _ in range(num_photos):
    cycle = cycle + 1
    file_name = os.path.join(folder, f"{object_name}_{cycle}.jpg")

    #take photo, save, and display
    frame = camera.capture_array()
    cv2.imwrite(file_name, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    display(Image(filename=file_name))
    time.sleep(0.5)

    #rotate platter
    easyGPG.turn_degrees(round(420/num_photos), blocking=False) #420 to account for motor imprecision
    time.sleep(1.5)

#LEDs and camera off
lights.fill((0, 0, 0))
lights.show()
camera.stop()
camera=None
print("Scan finished.")

### 2. Send to API

#verify token
token_info = OpenScanCloud("getTokenInfo", msg)

if token_info.status_code != 200:
    raise Exception(f"ERROR: token not verified {token_info.status_code}")

credit = token_info.json()["credit"]
print(f"Token verified. Credits left: {credit}.")

#check photo data
limit_file_size = token_info.json()["limit_filesize"]
limit_photos = token_info.json()["limit_photos"]

images = []
for image in os.listdir(folder):
    if os.path.splitext(image)[1] in allowed_extensions:
        images.append(image)

if len(images) == 0:
    raise Exception("ERROR: No images found")

file_size = 0
for image in images:
    file_size = file_size + os.path.getsize(os.path.join(folder, image))

msg["photos"] = len(images)

if file_size > limit_file_size or len(images) > limit_photos:
    raise Exception(f"ERROR: Photos too large! Max file size: {limit_file_size}. Max number of photos: {limit_photos}.")

print("Preparing images.")

#clean dir_temp folder
for i in os.listdir(dir_temp):
    try: os.remove(os.path.join(dir_temp, i))
    except: pass

project_name = str(int(time.time()*100))+ '-OSC.zip'
file = os.path.join(dir_temp, project_name)
msg["project"] = project_name

#zip images
with zipfile.ZipFile(file, "w") as zipf:
    for image in images:
        zipf.write(os.path.join(folder, image), image)

msg["filesize"] = os.path.getsize(file)
msg["partslist"] = [file]

#split up zip file if too large
if os.path.getsize(file) > size_to_split:
    msg["partslist"] = []
    number = 1
    with open(file, "rb") as f:
        chunk = f.read(size_to_split)
        while chunk:
            chunk_name = f"{file}_{number}"
            with open(chunk_name, "wb+") as chunk_file:
                chunk_file.write(chunk)
            msg["partslist"].append(chunk_name)
            number += 1
            chunk = f.read(size_to_split)
    os.remove(file)

msg["parts"] = len(msg["partslist"])

print("Sending images.")
r = OpenScanCloud("createProject", msg)
if r.status_code != 200:
    raise Exception("ERROR: Unable to create project")
ulinks = r.json()["ulink"]

#send zip file (parts)
for i, chunk_file_path in enumerate(msg["partslist"]):
    print(f"Uploading {i+1} of {len(msg["partslist"])} file(s).")
    with open(chunk_file_path, "rb") as f:
        data = f.read()
    r = requests.post(url=ulinks[i], data=data, headers={"Content-type": "application/octet-stream"})
    if r.status_code != 200:
        raise Exception("ERROR: Unable to send files")

print("Creating 3D model.")
r = OpenScanCloud("startProject", msg)
if r.status_code != 200:
    raise Exception("ERROR: Unable to start 3D model creation")

### 3. Extract download link from API and show 3D model on display

#check for 3D model download link
status_msg = {"token": token, "project": msg["project"]}

while True:
    time.sleep(30)
    r = OpenScanCloud("getProjectInfo", status_msg)
    if r.status_code != 200:
        print("ERROR: Unable to get scan info.")
        continue

    info = r.json()
    print("Scan info:", info)
    scan_status = info.get("status", "unknown")
    print(f"[{time.strftime("%X")}] Status: {scan_status}.")

    if scan_status == "processing done":
        time.sleep(10)
        dlink = info.get("dlink") #if Open Scan API returns dlink
        
        if not dlink: #if Open Scan API does not return dlink, use IMAP
            print("ERROR: No download link found. Using IMAP to find link.")
            time.sleep(20) #wait for email to send

            mail = imaplib.IMAP4_SSL(IMAP)
            mail.login(email_user, email_pass)
            mail.select("INBOX")

            #find latest email from Open Scan API
            status, messages = mail.search(None, '(FROM "cloud@openscan.eu")')
            if status == "OK" and messages[0]:
                newest = messages[0].split()[-1]
                _, data_message = mail.fetch(newest, "(RFC822)")
                target_message = email.message_from_bytes(data_message[0][1])

                text_message = ""
                for part in target_message.walk():
                    if part.get_content_type() in ["text/plain", "text/html"]:
                        text = part.get_payload(decode=True).decode(errors="ignore")
                        break
                        
                #get dlink from email
                links = re.findall(r'https?://[^\s"<]*openscan\.eu[^\s"<]*', text)
                if links:
                    dlink = links[0].replace("&amp;", "&")
                mail.logout()

        #extract dropbox zip download link
        parsed = urllib.parse.urlparse(dlink)
        qs = urllib.parse.parse_qs(parsed.query)

        dlink = qs["id"][0]

        if "dl=" not in dlink:
            dlink += "&dl=1"
        else:
            dlink = dlink.replace("dl=0", "dl=1")

        #download zip file from dropbox
        r = requests.get(dlink, allow_redirects=True)
        file_download = os.path.join(zip_scanned, os.path.basename(dlink))
        with open(file_download, "wb") as f:
            f.write(r.content)
        
        #extract zip file
        with zipfile.ZipFile(file_download, "r") as zip_r:
            zip_r.extractall(zip_extracted)
        print("ZIP Extraction complete!")

        #find .obj 3D model in extracted folder
        model = next((f for f in os.listdir(zip_extracted) if f.lower().endswith(".obj")), None)
        if not model:
            print("ERROR: No .obj 3D model found.")
            break
        else:
            path_model = os.path.join(zip_extracted, model)

            #display 3D model on F3D viewer
            ENV = os.environ.copy()
            ENV["WAYLAND_DISPLAY"] = "wayland-0"
            ENV["DISPLAY"] = ":0"
            ENV["XAUTHORITY"] = "/home/pi4/.Xauthority"
            subprocess.run(["f3d", "--resolution=760,400", "--position=20,70", path_model], env=ENV)
            print("Displaying 3D model!")
            break

    elif scan_status == "Processing failed":
        print("ERROR: Unable to create 3D model. Please try again.")
        break
