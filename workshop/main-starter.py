from digitalio import *
from board import *
import busio
from time import monotonic, sleep
from pixel import setPixel
from hologram import formatMsg, ip, port

DEVICEKEY = "NdWiNVXif"

RESET_PIN = DigitalInOut(D2)
RESET_PIN.direction = Direction.OUTPUT

# Global State
MODEM_STARTUP = False
MODEM_CONFIG = False
NET_CONNECT = False

def resetModem(resetPin):

    setPixel(0,0,255) # set RGB to blue

    # toggle RST pin
    resetPin.value = 1
    sleep(0.1)
    resetPin.value = 0
    sleep(0.1)
    resetPin.value = 1

    for x in range(0,45): # wait 45 seconds for modem to startup
        setPixel(0,0,0) # blink RGB
        sleep(0.5)
        setPixel(0,0,255)
        sleep(0.5)

def sendCommand(cmd, wait, success):
    # print helpful feedback with wait time
    print("CMD (~" + str(wait) + " seconds) " + cmd)
    result = uart.write(cmd)
    timeout = monotonic() + wait
    response = None

    while True:
        if monotonic() > timeout:
            break
        else:
            data = uart.read(64) # read response
            if data != None:
            	datastr = ''.join([chr(b) for b in data]) # convert bytearray to string
            	response = datastr
                break

    if success not in response:
        print("ERROR: " + cmd)
        print(response)
        return False
    else:
        return True

def disconnect():
    # Disconnect / shutdown modem connection
    if not sendCommand("AT+CIPSHUT\r\n", 65, "SHUT OK"):
        return False
    return True

def connect():
    # Shutdown modem before bringing it back up


    # Check GPRS status


    # Set modem mode


    # Set APN


    # Bring up wireless connection


    # Get local IP address


    return True

def sendMessage(message):
    # format message string


    # Start hologram TCP connection


    # Prepare modem to send


    # Send string to server


    # Wait for TCP session to close


    return True


########################################################
print("### MODEM STARTUP #############################")
########################################################

# UART send "AT\r\n"
uart = busio.UART(D4, D3, baudrate=19200)

# reset modem
print("Modem RST ~45 seconds")
resetModem(RESET_PIN)

MODEM_STARTUP = True

########################################################
print("### MODEM CONFIGURE #############################")
########################################################

while MODEM_STARTUP:

    # Check UART communication


    # Set cell modules baud rate


    # Check if SIM is readable


    # Set SMS to text mode


    print("### MODEM CONFIGURE SUCCESSFUL ###")
    MODEM_CONFIG = True
    break

########################################################
print("### NETWORK CONNECT #############################")
########################################################

if MODEM_CONFIG:

    if connect():
        print("### NETWORK CONNECT SUCCESSFUL ###")
        NET_CONNECT = True

########################################################
print("### SEND MESSAGE ################################")
########################################################

if NET_CONNECT:

    if sendMessage("Yay, We did it!"):
        print("### SEND MESSAGE SUCCESSFUL ###")

    disconnect()
