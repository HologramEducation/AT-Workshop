# Workshop Instructions

## Introduction

I work for [Hologram (the largest Cellular network provider for IoT)](https://hologram.io/devplan); nearly every day I get the chance to try out different cellular modems and modules. Each modem manufacturer has different commands they accept but what does not change is *how* they accept commands. 

Every cellular module/modem communicates through [AT Commands](wiki link). This makes it relatively simple to hook up UART TX/RX and start communicating with the modem. But as anyone who has dealt with cellular, the devil is in the details. 

This tutorial steps through a workshop I host at IoT conferences. Workshop participants walk through sending AT commands to the modem using CircuitPython. The goal of this workshop is to show everyone that AT commands are not a difficult thing and knowing how to communicate with modems is a useful  skill.

In the workshop, I hand out kits which include a [Hologram Developer SIM](https://hologram.io/devplan), [simCOM SIM800](https://www.aliexpress.com/item/I006-SIM800L-V2-0-5V-Wireless-GSM-GPRS-MODULE-Quad-Band-W-Antenna-Cable-Cap/32667378752.html) modem (which was probably the most popular 2G M2M modem ever made, and an [Adafruit Trinket M0](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino?view=all) (currently my favorite MCU). 

I hope you learn two things after this workshop.

  - How to work with the Trinket M0 (mass storage device, serial over USB, circuit python)
  - How to work with the SIM800 breakout (UART, AT commands, negotiating with cellular towers) 

Note: Since simCOM keeps their command structure relatively similar between modules, these commands will most likely work with the SIM808, SIM900, SIM7000 and others.

## Slides

**Title Slide**
![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.001.jpeg?raw=true)

**Requirements**
![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.003.jpeg?raw=true)

- Hologram Platform
- Adafruit Trinket M0
- Circuit Python
- simCOM SIM800 2G Breakout
- Any IDE/Text Editor
    - Recommend: VS Code w/PlatformIO
- Serial Monitor
    - Recommend: monitor built into PlaformIO, screen for Mac & Linux, PuTTY for Windows

**Activate the Hologram SIM**
![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.011.jpeg?raw=true)

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.013.jpeg?raw=true)

**Assemble the Kit**
![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.016.jpeg?raw=true)

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.017.jpeg?raw=true)

After the kit is wired and SIM is inserted then plug the USB into your computer. The Trinket's LED should blink blue. After 45 seconds the LED will turn *green* if you wired everything correctly and *red* if incorrect.

**Interacting with the Trinket**
![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.019.jpeg?raw=true)

If you are running Windows 7 make sure to install Adafruit's Windows Driver.

Once connected the Trinket should attach as a Mass Storage Device and accessible through your file browser.

Control the Trinket by modifying and saving the `main.py` file. The code will compile and execute as soon as you save the file.

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.018.jpeg?raw=true)

Fire up your Serial Monitor to see debugging logs from the script. Set baud rate to 19200. Mac port should be similar to `cu.usbmodem1451` and PC should be a `COM` port.

**Workshop Files**

1. Move files from the `/lib` folder of this repo into the `/lib` folder on the Trinket.
2. Move `workshop/begin-code/main.py` into the root of the Trinket.

Note: `workshop/begin-code/main.py` is a fill-in-the-blank (❓❓) version of the code. For reference, you can see the final code in `workshop/final-code/main.py`. 

**Edit the Files**

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.024.jpeg?raw=true)

Grab your cloud device key from the device detail page in https://dashboard.hologram.io. Edit the `DEVICEKEY` variable with the 8-character code from the dashboard.

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.023.jpeg?raw=true)

Next, we'll walk through the script from beginning to end, filling in each AT command along the way. The above slide describes the parameters of the `sendCommand()` function. Use this function when interacting with the modem. This function handles all the nuances and timeouts gracefully.

**Send the Commands!**

Each slide below shows a table. Each table contains the AT Command, timeout, success string and error string of each needed command. The step column corresponds to the comment in the code, shown before each sendCommand() function. Match the comment to the step number and fill-in the command parameters. 

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.025.jpeg?raw=true)

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.026.jpeg?raw=true)

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.027.jpeg?raw=true)

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.028.jpeg?raw=true)

**Check your Work**

If you wired everything up, replaced every ❓ in the script, inserted the SIM correctly, and saved it all to the Trinket, then you should see a success message on the serial monitor. 

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.029.jpeg?raw=true)

And if you see a success message in the Serial Monitor then your message should show up in the Hologram console too!

**Send an Inbound Message**

Your Trinket is also listening for inbound messages on port 4010. Go to the device detail page in the Hologram Dashboard and send a TCP message to your device. Does the message show up in the Serial Monitor?

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.030.jpeg?raw=true) 

**Take it Further**

In each workshop, we always have a few participants finish before everyone else. For those super developers, I challenge them to expand the script. Usually, 1-in-10 developers can do it in under 20 minutes. Are you one of those developers? 

- From the Hologram Dashboard create a new route that sends an SMS message to your phone each time the dashboard receives a message from your device.
- Create a while loop on the Trinket that listens for inputs from the Serial Monitor and sends that data up into the cloud. You should be able to send complete custom messages, not one character at a time.

If you were at my workshop and were able to demonstrate working solutions, then I would give you a free Hologram Nova. If you did it through this tutorial, all I can give you is a virtual high five 🙌 and say GREAT JOB!

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.031.jpeg?raw=true)

**WOOT - YOU DID IT**

![](https://github.com/benstr/AT-Workshop/blob/master/resources/presentation/image-export/AT-Workshop.032.jpeg?raw=true)
