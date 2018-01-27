from digitalio import *
from board import *
import busio
from time import monotonic, sleep
from pixel import setPixel
from hologram import formatMsg, ip, port

DEVICEKEY = "❓❓"

RESET_PIN = DigitalInOut(D2)
RESET_PIN.direction = Direction.OUTPUT

# Global State
STARTUP = False
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

def sendCommand(cmd, wait, success="OK", fail="ERROR"):
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
                if success or fail in datastr:
                    response = datastr
                    break

    if success in response:
        return True
    elif fail in response:
        print("ERROR: " + cmd)
        print(response)
        return False
    else:
        print("TIMEOUT: " + cmd)
        #print(response)
        return False


def disconnect():
    # C0 - Disconnect / shutdown modem connection
    if not sendCommand("AT+CIPCLOSE=1\r\n", 4, "CLOSE OK"):
        return False
    return True

def connect():
    # C1 - Shutdown modem before bringing it back up
    if not sendCommand("❓❓", ❓, "❓"):
        return False

    # Check signal strength
    # TODO parse return for signal strength, below is incorrect
    # if not sendCommand("AT+CSQ\r\n", 2, "OK"):
    #     return False

    # C2 - Check GPRS status
    if not sendCommand("❓❓", ❓):
        return False

    # C3 - Set modem mode
    if not sendCommand("❓❓", ❓):
        return False

    # C4 - Set APN
    if not sendCommand("❓❓", ❓):
        return False

    # C5 - Bring up wireless connection
    if not sendCommand("❓❓", ❓):
        return False

    # C6 - Get local IP address
    if not sendCommand("❓❓", ❓, "❓"):
        return False

    # C7 - Start inbound server
    if not sendCommand("❓❓", ❓, "❓"):
        return False

    return True

def sendMessage(message):
    # format message string
    fullMessage = formatMsg(message, DEVICEKEY)

    # C8 - Start hologram TCP connection
    if not sendCommand("❓❓❓", ❓, "❓", "❓"):
        return False

    # C9 - Set message length
    msgLength = len(fullMessage)
    if not sendCommand("❓❓", ❓, "❓"):
        return False

    # C10 - Send string to server
    if not sendCommand(❓, ❓, "❓", "❓"):
        return False

    return True

def sendResponse(responseMsg = "RECEIVE OK"):
    # C11 - Send a message back to server after receiving data
    if not sendCommand("❓❓", ❓, "❓"):
        return False

    # C12 - Send string to server
    if not sendCommand(❓, ❓, "❓"):
        return False

    return True

########################################################
print("### PROJECT STARTUP #############################")
########################################################

# UART send "AT\r\n"
uart = busio.UART(D4, D3, baudrate=19200)

# reset modem
print("Modem RST ~45 seconds")
resetModem(RESET_PIN)

STARTUP = True

########################################################
print("### MODEM CONFIGURE #############################")
########################################################

while STARTUP:

    # C13 - Check UART communication
    if not sendCommand("❓❓", ❓):
        break

    # C14 - Set cell modules baud rate
    if not sendCommand("❓❓", ❓):
        break

    # C15 - Check if SIM is readable
    if not sendCommand("❓❓", ❓):
        break

    # C16 - Set SMS to text mode
    if not sendCommand("❓❓", ❓):
        break

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

    if sendMessage("Yay, We did it! -benstr"):
        print("### SEND MESSAGE SUCCESSFUL ###")

    disconnect()

# ########################################################
# print("### RECEIVE MESSAGE #############################")
# ########################################################

while True:
    data = uart.read(64) # check for any inbound data

    if data != None and "+RECEIVE" in data:
        datastr = ''.join([chr(b) for b in data]) # convert bytearray to string
        print(datastr)
        sendResponse()

    sleep(5)
