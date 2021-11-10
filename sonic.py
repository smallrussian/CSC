import RPi.GPIO as GPIO
from time import sleep, time
#constatns
DEBUG=False
SETTLE_TIME=2   #seconds to let the sensor settle
CALIBRATIONS=5  #number of calibration measurements
CALIBRATION_DELAY=1 seconds to delay between them
#set the pi to the broadcom pin layout
GPIO.setmode(GPIO.BCM)
#GPIO pins
Trig=18#the sensors trig pin
Echo=27#the sensors echo pin
GPIO.setup(Trig, GPIO.OUT) #Trig is an outpit
GPIO.setup(Echo, GPIO.IN) #Echo is an input

#calibrate sensor with a correction factor
def calibrate():
    print("Calibrating")
    #prompt the user for an objet's known distance
    print("Place the sensor a known distance away from an object.")
    known_distance=float(input("What is the kown distance (cm)? "))
    # measure the distance to the object with the sensor
    # we do this several times and get an average
    print("Getting calibration measurements...")
    distance_avg = 0
    for i in range(CALIBRATIONS):
	    distance = getDistance()
	    if (DEBUG):
		    print("Got {}cm".format(distance))
	    # keep a running sum
	    distance_avg += distance
	    # delay a short time before using the sensor again
	    sleep(CALIBRATION_DELAY)

#uses sensor to calcualte the distance to an object
def getDistance():
    pass
########

#MAIN PROGRAM

#######
#first allow the sensor to settle for a bit
print("Wating for sensor to settle({}s".format(SETTLE_TIME))
GPIO.output(Trig, GPIO.LOW)
sleep(SETTLE_TIME) #seconds to let the sensor sett

#next calibrate the sensor
correction_factor=calibrate()
#then measure
#finally  cleanup the GPIO pins 