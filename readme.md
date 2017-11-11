# Workshop Instructions

## Requirements
- [Adafruit Trinket M0](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino?view=all)
  - [Windows 7 requires this driver](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino?view=all#windows-driver-installation)
- [simCOM SIM800L Breakout](https://www.aliexpress.com/item/I006-SIM800L-V2-0-5V-Wireless-GSM-GPRS-MODULE-Quad-Band-W-Antenna-Cable-Cap/32667378752.html)
- [Hologram Developer SIM](https://hologram.io/devplan)
- Recommended - [PlatformIO IDE](http://platformio.org/get-started)

## Steps

### 1. Setup

- [Activate Hologram SIM](https://dashboard.hologram.io/activate)
    - Generate CSRPSK Device Key and save it temporarily, we'll use it soon.
- Wire components
    - Remove power from Trinket
    - Wire from left to right on the modem
    - RST - 2
    - GND - GND
    - RXD - 4
    - TXD - 3
    - VDD - USB
    - GND - GND
    - 5VIN - USB
- Run `verify/main.py` to check if modem is wired correctly
    - Connect Trinket to computer
    - Replace `lib` folder with the one in this repo
    - Upload the `main.py` from this repo under `verify/main.py` to the boards root
    - Apply power.
    - You're all set if the board blinks BLUE then GREEN.
    - If the trinket blinks BLUE the RED you need to double check your wiring
    - Hint: You can open a serial monitor @ baud 115200 to see debug messages

## 2. Send a String

I've included a `resource/` folder in this repo containing SIMCOM AT command manuals.

- Open the TCP manual as a reference.
- Open `workshop/main-starter.py` in an IDE.
- I've commented where each modem command should go, the challenge is to try and fill it in :).
    - Rename file to `main.py`
    - Paste in your Device Key in the key variable near the top of the file
    - Go to each comment and try to discover what command needs to go there
        - Hint 1: Refer to the simCOM manuals
        - Hint 2: I've done the first one for you in the `disconnect()` function, around line 60.
- Check your work against my code in `workshop/main-final.py`
- Plug the trinket in and upload `main.py` as often as you like to check your progress
    - Make sure to open a serial monitor to watch debug messages
- Send a string message to the cloud

By the end you should have completed the following
- Configure the modem
- Connect to the cellular network
- Sent a message to the cloud
- Disconnected from the cloud

## 3. Receive a String

- Coming soon.... aka if I have time :)

## 4. Do more

As mentioned, the `resource/` folder contains SIMCOM AT command manuals. I would encourage you to skim the table of contents and try anything interesting.

Some suggestions:
- Cell locate: Use cell tower triangulation to determine you approximate coordinates
- Send and receive SMS messages
- Use UDP instead of TCP
