from digitalio import *
from board import *
import busio
from time import monotonic, sleep
from pixel import setPixel
from hologram import formatMsg, ip, port

DEVICEKEY = "NdWiNVXi"

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

def sendCommand(cmd, wait, success, fail="ERROR"):
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
                if success or fail in response:
                    break

    if fail in response:
        print("ERROR: " + cmd)
        print(response)
        return False
    elif success in response:
        return True
    else:
        print("TIMEOUT: " + cmd)
        return False


def disconnect():
    # Disconnect / shutdown modem connection
    if not sendCommand("AT+CIPCLOSE=1\r\n", 4, "CLOSE OK"):
        return False
    return True

def connect():
    # Shutdown modem before bringing it back up
    if not sendCommand("AT+CIPSHUT\r\n", 65, "SHUT OK"):
        return False

    # Check signal strength
    # TODO parse return for signal strength, below is incorrect
    # if not sendCommand("AT+CSQ\r\n", 2, "OK"):
    #     return False

    # Check GPRS status
    if not sendCommand("AT+CGATT?\r\n", 10, "OK"):
        return False

    # Set modem mode
    if not sendCommand("AT+CIPMUX=1\r\n", 2, "OK"):
        return False

    # Set APN
    if not sendCommand("AT+CSTT=\"hologram\"\r\n", 2, "OK"):
        return False

    # Bring up wireless connection
    if not sendCommand("AT+CIICR\r\n", 85, "OK"):
        return False

    # Get local IP address
    if not sendCommand("AT+CIFSR\r\n", 2, "."):
        return False

    # Start inbound server
    if not sendCommand("AT+CIPSERVER=1,4010\r\n", 2, "SERVER OK"):
        return False

    return True

def sendMessage(message):
    # format message string
    fullMessage = formatMsg(message, DEVICEKEY)

    # Start hologram TCP connection
    if not sendCommand("AT+CIPSTART=1,\"TCP\",\"" + ip() + "\",\"" + port() + "\"\r\n", 75, "OK", "FAIL"):
        return False

    # Set message length
    msgLength = len(fullMessage)
    if not sendCommand("AT+CIPSEND=1," + str(msgLength) + "\r\n", 5, ">"):
        return False

    # Send string to server
    if not sendCommand(fullMessage, 60, "OK", "FAIL"):
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

    # Check UART communication
    if not sendCommand("AT\r\n", 3, "OK"):
        break

    # Set cell modules baud rate
    if not sendCommand("AT+IPR=19200\r\n", 5, "OK"):
        break

    # Check if SIM is readable
    if not sendCommand("AT+CPIN?\r\n", 5, "OK"):
        break

    # Set SMS to text mode
    if not sendCommand("AT+CMGF=1\r\n", 10, "OK"):
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

    if sendMessage("Yay, We did it!"):
        print("### SEND MESSAGE SUCCESSFUL ###")

    disconnect()

# ########################################################
# print("### RECEIVE MESSAGE #############################")
# ########################################################

while True:
    data = uart.read(64) # check for any inbound data
    if data != None:
        datastr = ''.join([chr(b) for b in data]) # convert bytearray to string
        print(datastr)
    sleep(5)
