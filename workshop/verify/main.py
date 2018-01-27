from digitalio import *
from board import *
import busio
from time import sleep
from pixel import setPixel

# Modem UART
uart = busio.UART(D4, D3, baudrate=19200)

print("Welcome to the AT Workshop ... lets check your wiring")

# reset modem
reset = DigitalInOut(D2)
reset.direction = Direction.OUTPUT

print("Step 1: Reset Modem (~45 seconds ugh!)")
setPixel(0,0,255) # set RGB to blue

# toggle RST pin
reset.value = 1
sleep(0.1)
reset.value = 0
sleep(0.1)
reset.value = 1

for x in range(0,45): # wait 45 seconds for modem to startup
    setPixel(0,0,0) # blink RGB
    sleep(0.5)
    setPixel(0,0,255)
    sleep(0.5)
    
print("Reset Finished")

# send AT command
print("Step 2: Sent Command:")
command = "AT\r\n"
result = uart.write(command)
print(str(result) + " bytes written")

sleep(2) # wait for a response

data = uart.read(8) # read response

if data != None: # if there is data from the modem then print
    setPixel(0,255,0)
    print("SUCCESS! Modem Responsed:")
    datastr = ''.join([chr(b) for b in data]) # convert bytearray to string
    print(datastr)
else: # if there is not data form the modem then set RGB red
    setPixel(255,0,0)
    print("FAIL! Modem DID NOT Respond")

print("This concludes the test")

sleep(60*10)
