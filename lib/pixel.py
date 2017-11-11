from board import APA102_SCK, APA102_MOSI
from busio import SPI
from time import sleep

# Istantiate DotStar LED
dotstar = SPI(APA102_SCK, APA102_MOSI)

def setPixel(red, green, blue):
    if not dotstar.try_lock():
        return

    data = bytearray([0x00, 0x00, 0x00, 0x00,
                      0xff, blue, green, red,
                      0xff, 0xff, 0xff, 0xff])
    dotstar.write(data)
    dotstar.unlock()
    sleep(0.01)
