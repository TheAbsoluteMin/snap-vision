# Firmware Installations

## Install GoPiGo3
In the Pi terminal, type the commands:

> mkdir -p ~/.venv && python3 -m venv ~/.venv/robotics

> ~/.venv/robotics/bin/pip install mr-gopigo3

> source ~/.venv/robotics/lib/python3.*/site-packages/gopigo3/scripts/install_trixie.sh

## (Optional) Install Jupyter Lab for coding
In the Pi terminal, type the commands:

> ~/.venv/robotics/bin/pip install jupyterlab

> ~/.venv/robotics/bin/jupyter lab --ip=0.0.0.0 --no-browser

The latter starts the web server broadcast. In order to open it up, you can type the access and token link displayed on the Pi terminal.

To have the server run in the background every time, create an automation file in the Pi terminal with the command:
> sudo nano /etc/systemd/system/jupyter.service

Then, type the following setup text inside: 

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

Congrats! Now you can code wirelessly in Jupyter Lab!

## Install firmware libraries

Type the following commands in the Pi terminal:

> sudo apt update && sudo apt install f3d -y

> sudo apt update && sudo apt install -y python3-picamera2

> sudo apt update && sudo apt install -y swig

> sudo apt update && sudo apt install -y liblgpio-dev

> ~/.venv/robotics/bin/pip install jupyterlab mr-gopigo3 opencv-python adafruit-circuitpython-dotstar

Now, type in:

> nano ~/.venv/robotics/pyvenv.cfg

and change the word "false" in "include-system-site-packages = false"
<img width="1331" height="219" alt="image" src="https://github.com/user-attachments/assets/c68a1370-9dcb-429e-a3cc-5ff22f8054e0" />
to "true"
<img width="1365" height="290" alt="image" src="https://github.com/user-attachments/assets/adfc8d73-ef69-4573-b3e0-a38f5778d8db" />
then hit Ctrl+O, Enter key, and Ctrl+X to save and exit.

## Flash main firmware

If you are coding in Jupyter Lab, you can run the code directly on its web server. Otherwise, you can download scan.py onto your Pi 4 from [here](https://github.com/TheAbsoluteMin/snap-vision/blob/main/firmware/scan.py).

Before running the firmware, ensure you add your API token, which can be obtained by emailing the official Open Scan API email at cloud@openscan.eu. If you want to ensure SnapVision works all the time, please add your Gmail address and Gmail app password in case Open Scan API does not return a valid download link in its dlink endpoint.
