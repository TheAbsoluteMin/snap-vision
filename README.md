# snap-vision

# Instructions

## Set up hardware
1. Connect the Pi Camera Model 3 to the Raspberry Pi 4 with an FFC ribbon cable with the cable clips. Make sure you connect to the Pi 4's "CAMERA" cable clip.
2. Connect the Hosyond DSI Display to the Raspberry Pi 4 with another FFC ribbon cable with the cable clips. Make sure you connect to the Pi 4's "DISPLAY" cable clip.
3. Attach the Dexter GoPiGo3 red board on top of the Raspberry Pi 4 with the screws and their standoffs.
4. Connect the DC motor with rotary magnetic encoder to the Dexter GoPiGo3 red board with the JST connector wires. Make sure you connect to the left JST connector port on the red board.
5. Attach the LED strip to the jumper wires (for extension) and wire them to the red board as shown below.
6. After following the Raspberry Pi 4 set up below, the battery pack can be connected to the red board's barrel jack. Remember, when powering on, always turn on the battery pack into the barrel jack before pressing the power button on the red board to start up the Pi 4. When turning off, press the power button on the red board before turning off the battery pack.

## Set up Raspberry Pi 4 with USB drive (and micro SD card without external micro SD card writer)

### Download Pi OS (64 Bit)
On your windows computer go to https://www.raspberrypi.com/software/operating-systems/ and download the file. You should get a download with a name similar to "raspios-trixie-arm64.img.xz".
<img width="1187" height="1111" alt="image" src="https://github.com/user-attachments/assets/d6bd0128-90d5-4a14-ac1d-d37a667cbfe6" />

### Download Rufus
Go to https://rufus.ie/en/ and download the file for windows.
<img width="1251" height="924" alt="image" src="https://github.com/user-attachments/assets/e352a57c-ce10-4714-9003-5001dd96c2e4" />

### Flash USB drive
Plug in a clean USB drive into a USB port on your computer, and open the Rufus application. Make sure your USB drive is selected under "Device". Press "SELECT" and select the Pi OS download. Press "START", and wait until the flashing is complete, which is signaled when the "STATUS" says "READY" after flashing.

<img width="876" height="1026" alt="image" src="https://github.com/user-attachments/assets/a242f4f7-9973-4c9e-8cec-a510f94a8b66" />

### Set up Raspberry Pi 4
If you want to transfer the USB drive data to a microSD without an external micro SD card writer, ensure you leave the micro SD card NOT plugged into the Pi 4. Plug the USB drive into a blue USB3.0 port in the Pi 4, and plug in a powerful USB-C charging cable into the Pi 4's USB-C port. It is recommended that you use the DSI display and a mouse and keyboard plugged into the USB2.0 ports, so you can then follow the instructions to set up your Pi 4's preferences.

### Optional: Flash the Pi OS onto a micro SD card
After your Pi 4 boots into its virtual desktop, you can plug in the micro SD card into the Pi 4's micro SD slot. Open Pi Imager by clicking on the Raspberry Pi icon, clicking Accessories, and then clicking Raspberry Pi Imager. Select Raspberry Pi 4 as the device, and Raspberry Pi OS (64-bit) as the OS. Continue to "Storage" and select your SD card. You can then follow the additional instructions to set up preferences for your SD card. Enabling SSH is recommended for coding wirelessly. Click "Write" when you are finished.

After writing, exit out of the Raspberry Pi Imager and enter the terminal. Type the command:
> sudo poweroff

and unplug the USB flash drive and USB-C charger cable. You can now plug in power from the battery pack into the GoPiGo3 red board's barrel jack.

## Install GoPiGo3
In the Pi terminal, type the commands:
> python3 -m venv ~/.venv/gopigo3

> ~/.venv/gopigo3/bin/pip install mr-gopigo3

> source ~/.venv/gopigo3/lib/python3.*/site-packages/gopigo3/scripts/install_trixie.sh

## Optional: Install Jupyter Lab for coding
In the Pi terminal, type the commands:
> mkdir -p ~/.venv && python3 -m venv ~/.venv/robotics

> ~/.venv/robotics/bin/pip install jupyterlab mr-gopigo3

> ~/.venv/robotics/bin/jupyter lab --ip=0.0.0.0 --no-browser

The latter starts the web server broadcast. In order to open it up, you can type the access and token link displayed on the Pi terminal.

To have the server run in the background every time, create an automation file in the Pi terminal with the command "sudo nano /etc/systemd/system/jupyter.service". Type the following setup text inside: 
> [Unit]

> Description=Jupyter Lab Robot Server

> After=network.target

> [Service]

> Type=simple

> User=gopigo

> WorkingDirectory=/home/gopigo

> ExecStart=/home/gopigo/.venv/robotics/bin/jupyter lab --ip=0.0.0.0 --no-browser

> Restart=always

> RestartSec=10

> [Install]

> WantedBy=multi-user.target"

Make sure you replace "gopigo" as needed if you changed your Pi 4's username. Save and exit with Ctrl+O, Enter key, and Ctrl+X. Run the commands in the terminal to finish:
> sudo systemctl daemon-reload

> sudo systemctl enable --now jupyter.service

Congrats! Now you can code wirelessly in Jupyter Labs!

## Build case

## Flash firmware

## Execute code

> sudo apt update

> sudo apt update && sudo apt install -y python3-picamera2

> sudo apt update && sudo apt install -y swig

> sudo apt update && sudo apt install -y liblgpio-dev

> ~/.venv/robotics/bin/pip install jupyterlab mr-gopigo3 opencv-python adafruit-circuitpython-dotstar

now do

> nano ~/.venv/robotics/pyvenv.cfg

and change false in "include-system-site-packages = false"
<img width="1331" height="219" alt="image" src="https://github.com/user-attachments/assets/c68a1370-9dcb-429e-a3cc-5ff22f8054e0" />
to true
<img width="1365" height="290" alt="image" src="https://github.com/user-attachments/assets/adfc8d73-ef69-4573-b3e0-a38f5778d8db" />
then hit Ctrl+O, Enter key, and Ctrl+X to save and exit.
