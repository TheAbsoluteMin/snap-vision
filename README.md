# SnapVision
Automated 3D scanner utilizing photogrammetry.


## See it in action
Demonstration link.

## Inspiration
Designing cases or models for real world parts through CAD can be difficult without exact measurements and dimensions. Obtaining such measurements and replicating intricate designs on some objects and electronic modules can also be tedious. Thus, I decided to build an automated 3D scanner that uses photogrammetry. With custom firmware and access to Open Scan API, SnapVision seeks to make the 3D scanning process hands-free and streamlined after the initial run of the firmware. I hope this project can potentially expedite the engineering and design processes.

## Features
* High resolution camera
* Interactive display screen
* Portable, sleek case design
* Heat escape grills
* Internal LEDs
* Powerful yet stable motor
* Fully integrated and automated API processing
* Real-time feedback during use

## Firmware Logic
1. Scanning
    1. Take a photo of the object
    2. Rotate object
    3. Repeat
<img width="1513" height="535" alt="image" src="https://github.com/user-attachments/assets/c94820a6-6832-42ee-b721-15a2f3c652da" />

2. Send images to API
    1. Verify API token
    2. Check photo data requirements
    3. Compress images in ZIP file(s)
    4. Send images
<img width="1485" height="531" alt="image" src="https://github.com/user-attachments/assets/75a1adc1-785d-4754-8899-9f642515badf" />

3. Extract the 3D model from API
    1. Check API processing status every 30 seconds
        1. If success:
            1. Get downloadable Dropbox link
            2. Download ZIP file
            3. Find .obj 3D model file
            4. Show 3D model on display screen
        2. If failure:
            1. Try again
<img width="1333" height="577" alt="image" src="https://github.com/user-attachments/assets/da338e0b-567c-4ece-a90d-a22991215de3" />

## Hardware
SnapVision uses some parts from the GoPiGo3 while integrating external components, including the Raspberry Pi 4, LED strip, and Hosyond 5 inch display screen. The following is a full wiring diagram.


## CAD Case
3D model [link](https://cad.onshape.com/documents/4bb380a378ec8b5d44400d73/w/f93c1e6eb205d04d3b317060/e/29820a57393d4c7f3e63d056?renderMode=0&uiState=6a73d4c936d5df3b8f23dfd1).

The case design evolved heavily from the first design.

<img width="659" height="859" alt="image" src="https://github.com/user-attachments/assets/00fdd98b-a99a-4c53-b9e6-a51178c269a9" />

Issues with space and hardware integration in the first design called for a remake. The second and final design was inspired by the Formlabs 3D printer design. 

<img width="813" height="882" alt="image" src="https://github.com/user-attachments/assets/ecc94b7b-b568-4302-aa3f-bfc5f9a7587c" />
<img width="943" height="1008" alt="image" src="https://github.com/user-attachments/assets/c22eac14-78e4-4742-8dde-7bda896df4fd" />

## BOM
| Part Name | Quantity | Price | Where to Buy |
| :--- | :---: | :---: | :--- |
| GoPiGo3 | 1 | $199.00 | [GoPiGo](https://gopigo.io/gopigo/) |
| Raspberry Pi 4 | 1 | $40.34 | [Vilros](https://vilros.com/products/raspberry-pi-4-model-b-1?src=raspberrypi) |

## How to use
1. Make sure SnapVision is in a well-lit place.
2. Run the main firmware at [scan.py](https://github.com/TheAbsoluteMin/snap-vision/blob/main/firmware/scan.py) (python) or scan.ipynb (Jupyter Lab) on the Raspberry Pi 4.
3. Place an object to be scanned inside SnapVision and on top of its platter.
4. Fill in the firmware prompts by typing in the object's name and the number of photos to be taken.
5. Watch SnapVision take photos, and wait until SnapVision finishes processing them with the Open Scan API.
6. Wait for a success message and a 3D model preview of your completed scan!

## Full assembly
<details>
<summary>
  <h3>A. Set up hardware</h3>
</summary>

1. Connect the Pi Camera Model 3 to the Raspberry Pi 4 with an FFC ribbon cable with the cable clips. Make sure you connect to the Pi 4's "CAMERA" cable clip.

<img width="4000" height="3000" alt="20260804_204716" src="https://github.com/user-attachments/assets/381037ac-3754-493a-809b-afdb01468161" />

2. Connect the Hosyond DSI Display to the Raspberry Pi 4 with another FFC ribbon cable with the cable clips. Make sure you connect to the Pi 4's "DISPLAY" cable clip.

<img width="4000" height="3000" alt="20260804_204956" src="https://github.com/user-attachments/assets/3fa1609b-91fe-41a6-bacd-666f98deb2d2" />

3. Attach the screws and standoffs on the Raspberry Pi 4.

<img width="4000" height="3000" alt="20260804_205245" src="https://github.com/user-attachments/assets/7755ed67-b9b2-4b3c-b356-519e30494b26" />

4. Attach the Dexter GoPiGo3 red board on top of the Raspberry Pi 4.

<img width="4000" height="3000" alt="20260804_210240" src="https://github.com/user-attachments/assets/987d4db3-8e7c-475a-8b28-80f536ea9dee" />

5. Connect the DC motor with rotary magnetic encoder to the Dexter GoPiGo3 red board with the JST connector wires. Make sure you connect to the left JST connector port on the red board.

<img width="4000" height="3000" alt="20260804_210528" src="https://github.com/user-attachments/assets/67edb018-2529-4ea9-9e3a-b253c5840b9b" />

6. Attach the LED strip to the jumper wires (for extension) and wire them to the red board as shown below.

<img width="4000" height="3000" alt="20260804_210837" src="https://github.com/user-attachments/assets/394d5883-8881-4f51-a06f-2b0aebbf04d3" />
<img width="4000" height="3000" alt="20260804_211317" src="https://github.com/user-attachments/assets/f1dca5d1-d022-46e4-8532-7929ee5d0b6e" />
<img width="4000" height="3000" alt="20260804_211240" src="https://github.com/user-attachments/assets/5e4ee197-9d9a-4268-9efa-a984c8d34416" />

7. After following the Raspberry Pi 4 set up below, the battery pack can be connected to the red board's barrel jack. Remember, when powering on, always turn on the battery pack into the barrel jack before pressing the power button on the red board to start up the Pi 4. When turning off, press the power button on the red board before turning off the battery pack.

<img width="4000" height="3000" alt="20260804_211535" src="https://github.com/user-attachments/assets/20380dc7-73e5-43d9-8e6e-ca4aca090e2e" />
</details>

<details>
<summary>
  <h3>B. Install Pi OS</h3>
</summary>
    
If you already have Pi OS installed on your Raspberry Pi 4, you can skip this step. For more help, visit this [guide](https://github.com/TheAbsoluteMin/snap-vision/blob/main/docs/Raspberry_Pi_OS_Setup.md).
</details>

<details>
<summary>
  <h3>C. Install firmware</h3>
</summary>

1. Install GoPiGo3

In the Pi terminal, type the commands:

> mkdir -p ~/.venv && python3 -m venv ~/.venv/robotics

> ~/.venv/robotics/bin/pip install mr-gopigo3

> source ~/.venv/robotics/lib/python3.*/site-packages/gopigo3/scripts/install_trixie.sh

2. (Optional) Install Jupyter Lab for coding

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

3. Install firmware libraries

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

4. Flash main firmware

If you are coding in Jupyter Lab, you can run the code directly on its web server. Otherwise, you can download scan.py onto your Pi 4 from [here](https://github.com/TheAbsoluteMin/snap-vision/blob/main/firmware/scan.py).
</details>

<details>
<summary>
  <h3>D. Final Assembly</h3>
</summary>

You can reference the model assembly here: https://cad.onshape.com/documents/4bb380a378ec8b5d44400d73/w/f93c1e6eb205d04d3b317060/e/29820a57393d4c7f3e63d056?renderMode=0&uiState=6a73d71636d5df3b8f23e703

Important: Please note that this guide assumes the color-coded parts, specifically the laser-cutted and 3D printed ones that were originally used.

Laser-cut parts can be found [here](https://github.com/TheAbsoluteMin/snap-vision/tree/main/CAD/Laser_Cutting). The parts with "Lid" or "Clear" in their name were cut in 3mm thick clear acrylic. The parts with "Internal" were cut in 3mm thick wood. All other laser-cut parts were cut in black acrylic.

3D printed parts can be found [here](https://github.com/TheAbsoluteMin/snap-vision/tree/main/CAD/3D_Printing).

However, you are able to 3D print everything.

1. Hot glue the following pieces together.
<img width="1180" height="758" alt="image" src="https://github.com/user-attachments/assets/ebd79d18-f341-4367-9850-05ced2f4b634" />
<img width="1585" height="716" alt="image" src="https://github.com/user-attachments/assets/40bdf591-5dfe-471d-a14b-98e9edf362e1" />
<img width="1240" height="725" alt="image" src="https://github.com/user-attachments/assets/9e818377-16e7-4c57-9142-e4ed5c76720d" />
<img width="1352" height="605" alt="image" src="https://github.com/user-attachments/assets/065f4f31-799d-427b-9bc6-d69474762a22" />
2. Assemble and hot glue the bottom case together.
<img width="1116" height="981" alt="image" src="https://github.com/user-attachments/assets/e36f0972-2a5b-429b-a8aa-b6cdf4e8c56e" />
3. Assemble and hot glue the top lid.
<img width="1409" height="763" alt="image" src="https://github.com/user-attachments/assets/16b2a2e4-20cb-4d6f-b22c-1ba2033d30e7" />
4. Assemble and hot glue the top case together. Make sure the 3D printed gray piece is in the back.
<img width="1212" height="1064" alt="image" src="https://github.com/user-attachments/assets/5ac3faa9-72ef-48fe-bf74-0cbe51bad660" />
5. Hot glue the second floor parts together.
<img width="1610" height="1001" alt="image" src="https://github.com/user-attachments/assets/4e793b8e-5100-4a39-8d5a-f01efeac41da" />
6. Hot glue the motor support in the 7th rectangular hole from the bottom in the bottom case's sides.
<img width="1507" height="1025" alt="image" src="https://github.com/user-attachments/assets/2da6011c-9864-4ecb-af3d-472449a7aad0" />
7. Place all the hardware inside the bottom case, and snap on the back bottom piece. That piece is the door to the power.
<img width="3000" height="4000" alt="20260804_220028" src="https://github.com/user-attachments/assets/92ae6486-259c-42d3-b483-ebcaec6ce714" />
8. Attach the platter onto the DC motor.
<img width="815" height="543" alt="image" src="https://github.com/user-attachments/assets/75814cd8-3ad8-4379-abfb-5f5cbea8ea9d" />
9. Snap on the second floor parts together. Make sure the motor is taped or glued to the motor support.
<img width="1315" height="800" alt="image" src="https://github.com/user-attachments/assets/6f67ca96-82e8-4fd8-92d6-3cfabb4b8481" />
10. Put together the camera using the Dexter camera mount.
<img width="4000" height="3000" alt="20260804_220932" src="https://github.com/user-attachments/assets/1c4bfe47-5ad9-4101-b1b5-119832436e63" />
11. Snap on the top case and top lid onto the second floor, and attach the Hosyond DSI display in the front.
<img width="3000" height="4000" alt="20260804_225511" src="https://github.com/user-attachments/assets/9bf2987e-2721-49b7-bb26-1ae16a974a10" />
</details>

## Credits
Thank you to the following:
- HackClub, for the opportunity and motivation to learn to build hardware projects!
- Tufts University Engineering Design Lab program, for access to instruction and fabrication materials!
- Ryan, for your support and contributions noted in the [JOURNAL.md](https://github.com/TheAbsoluteMin/snap-vision/blob/main/JOURNAL.md), specifically in the firmware and assembly of SnapVision!
- Thomas Megel from OpenScanCloud, for access to an API key and his example API code!
