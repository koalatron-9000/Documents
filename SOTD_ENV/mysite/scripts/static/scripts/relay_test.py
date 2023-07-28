#imports
import RPi.GPIO as GPIO
import sys
import digitalio
import board

#pin initialization
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
switch = digitalio.DigitalInOut(board.D17)
switch.direction = digitalio.Direction.OUTPUT
def relay_switch(x):
    if isinstance(x, int):
        if x == 1:
            #GPIO.output(11,1)
            switch.value = True
            print("On!")
        if x == 0:
            #GPIO.output(11,0)
            switch.value = False
            print("Off!")
    else:
        if str(x[1]) =="1":
            #GPIO.output(11,1)
            switch.value = True
            print("On!")
        if str(x[1]) == "0":
            #GPIO.output(11,0)
            switch.value = False
   
if __name__ == "__main__":
    relay_switch(sys.argv)  
