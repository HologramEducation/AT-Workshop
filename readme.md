# Workshop Instructions

## Step 1: setup

- Install PlatformIO (expands Atom IDE)
- Clone repo: TBD
- Power Trinket M0
- Open PlatformIO (cd into trinket drive then run atom .)
- Open Serial Monitor (usbmodem... @ baud 115200)
- Comment out line 83 in main.py and save (observe the instant compile)
- Touch D3 on trinket to see response

## Step 2: wire-up modem

- Remove power from Trinket
- Wire from left to right on the modem
- RST - 2
- GND - GND
- RXD - 4
- TXD - 3
- VDD - USB
- GND - GND
- 5VIN - USB
- Connect Trinket
- Replace main.py on the board with step-2/main.py from this repo

## Step 3: Send a string

- 
