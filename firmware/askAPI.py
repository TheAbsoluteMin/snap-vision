import os
import subprocess
import time
import zipfile
import io
import requests

key = "key"
folder = "/home/pi/snap_vision_photos/"
urlBase = "https://cloud.openscan.eu:5000"

#find images
print("find images")
zipNew = io.BytesIO()
with zipfile.ZipFile(zipNew, "w", zipfile.ZIP_DEFLATED) as zipImages:
    for file in os.listdir(folder):
        if file.endswith(".jpg"):
            pathFile = os.path.join(folder, file)
            zipImages.write(pathFile, arcname=file)
zipNew.seek(0)

#API time
print("uploading to API")
urlAsk = f"{urlBase}/load_project"
head = {"Authorization": "Bearer " + key}
fields = {"project_name": "snap_vision"}
zipSend = {"file": ("snap_vision.zip", zipNew, "application/zip")}

askAPI = requests.post(urlAsk, headers=head, data=fields, files=zipSend)
answerAPI = askAPI.json()
project_id = answerAPI["project_id"]

print("ask for 3D model")
status = "processing"
urlStatus = f"{urlBase}/get_project_status"
while status != "completed":
    time.sleep(30)
    askModel = requests.post(urlStatus, headers=head, json={"project_id": project_id})
    answerModel = askModel.json()
    status = answerModel.get("status", "processing")
    print(status)

    if status == "error":
        print("error")
        exit()

print("get 3D model")
urlGet = f"{urlBase}/download_project"
zipGet = requests.post(urlGet, headers=head, json={"project_id": project_id})
zipOut = "/home/pi/model.zip"
with open(zipOut, "wb") as CAD:
    CAD.write(zipGet.content)

print("show model")
extractFolder = "/home/pi/model_see/"
with zipfile.ZipFile(zipOut, "r") as zipSee:
    zipSee.extractall(extractFolder)
subprocess.run(["f3d", os.path.join(extractFolder, "mesh.stl")])

