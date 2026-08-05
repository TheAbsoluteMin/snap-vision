# Raspberry Pi OS Setup

## Already have it
If you already have the OS installed, you can skip this guide!

## Normal Setup with SD card reader
Follow the official guide at https://www.raspberrypi.com/documentation/computers/getting-started.html.

## Setup without SD card reader (with USB drive and optionally a micro SD card)

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
If you want to transfer the USB drive data to a microSD without an external micro SD card reader, ensure you leave the micro SD card NOT plugged into the Pi 4. Plug the USB drive into a blue USB3.0 port in the Pi 4, and plug in a powerful USB-C charging cable into the Pi 4's USB-C port. It is recommended that you use the DSI display and a mouse and keyboard plugged into the USB2.0 ports, so you can then follow the instructions to set up your Pi 4's preferences.

### Optional: Flash the Pi OS onto a micro SD card
After your Pi 4 boots into its virtual desktop, you can plug in the micro SD card into the Pi 4's micro SD slot. Open Pi Imager by clicking on the Raspberry Pi icon, clicking Accessories, and then clicking Raspberry Pi Imager. Select Raspberry Pi 4 as the device, and Raspberry Pi OS (64-bit) as the OS. Continue to "Storage" and select your SD card. You can then follow the additional instructions to set up preferences for your SD card. Enabling SSH is recommended for coding wirelessly. Click "Write" when you are finished.

After writing, exit out of the Raspberry Pi Imager and enter the terminal. Type the command:
> sudo poweroff

and unplug the USB flash drive and USB-C charger cable. You can now plug in power from the battery pack into the GoPiGo3 red board's barrel jack.
