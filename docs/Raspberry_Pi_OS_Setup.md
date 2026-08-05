# Raspberry Pi OS Setup

## Already have it
If you already have the OS installed, you can skip this guide!

## Quick setup with SD card reader
Follow the official guide at https://www.raspberrypi.com/documentation/computers/getting-started.html.

## Advanced setup without SD card reader
Use this method if you only have a USB drive (and optionally a microSD card).

### 1. Download Pi OS (64 Bit)
- Go to the [Raspberry Pi Software Page](https://www.raspberrypi.com/software/operating-systems/).
- Download the 64-bit installer.
- You should get a download with a name similar to "raspios-trixie-arm64.img.xz"
<img width="1187" height="1111" alt="image" src="https://github.com/user-attachments/assets/d6bd0128-90d5-4a14-ac1d-d37a667cbfe6" />

### 2. Download Rufus
- Go to [Rufus.ie](https://rufus.ie/en/).
- Download the latest Windows version.
<img width="1251" height="924" alt="image" src="https://github.com/user-attachments/assets/e352a57c-ce10-4714-9003-5001dd96c2e4" />

### 3. Flash USB drive
- Plug a clean USB drive into your windows computer.
- Open Rufus.
- Select your USB drive under Device.
- Click SELECT and choose your downloaded Pi OS file.
- Click START.
- Wait for STATUS to show READY after flashing, which means it is done.
<img width="876" height="1026" alt="image" src="https://github.com/user-attachments/assets/a242f4f7-9973-4c9e-8cec-a510f94a8b66" />

### 4. Boot the Raspberry Pi 4
- Important: If copying data to a microSD card later, do not insert the microSD card yet.
- Plug the flashed USB drive into a blue USB 3.0 port.
- (Optional) Connect the DSI display, mouse, and keyboard into the black USB 2.0 ports, which can help with setup.
- Power on the Pi itself using a high-quality USB-C power cable and its USB-C port.
- Follow the prompts to complete your preferences setup.

### 5. (Optional) Copy OS to micro SD card
- Insert your microSD card into the Pi 4's card slot.
- Open the Raspberry Pi Imager application: Raspberry Pi Icon ➔ Accessories ➔ Raspberry Pi Imager.
- Set Device to Raspberry Pi 4.
- Set Operating System to Raspberry Pi OS (64-bit).
- Click Storage and select your micro SD card.
- Set your preferences.
- (Recommended) Enable SSH to allow wireless coding.
- Click Write
- After writing, exit out of the Raspberry Pi Imager and enter the Pi terminal.
- Type the command:
> sudo poweroff
- Unplug the USB flash drive and USB-C charger cable.
- You can now plug in power from the battery pack into the GoPiGo3 red board's barrel jack.
