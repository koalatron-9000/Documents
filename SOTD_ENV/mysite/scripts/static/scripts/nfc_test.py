import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.spi import PN532_SPI
import relay_test
import time


# SPI connection:
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)
ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()
print("Waiting for RFID/NFC card...")
while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    print(".", end="")
    # Try again if no card is available.
    if uid is None:
        relay_test.relay_switch(0)
        time.sleep(2)
        continue

    print("Found card with UID:", [hex(i) for i in uid])
    relay_test.relay_switch(1)
    time.sleep(2)