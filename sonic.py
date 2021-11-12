import RPi.GPIO as GPIO
from time import sleep, time
#constatns
DEBUG=False
SETTLE_TIME=2   #seconds to let the sensor settle
CALIBRATIONS=5  #number of calibration measurements
CALIBRATION_DELAY=1 #seconds to delay between them
TRIGGER_TIME=.00001
SPEED_OF_SOUND=343
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
        # calculate the average of the distances
    distance_avg /= CALIBRATIONS
    if (DEBUG):
	    print("Average is {}cm".format(distance_avg))
    # calculate the correction factor
    correction_factor = known_distance / distance_avg
    if (DEBUG):
	    print("Correction factor:{}".format(correction_factor))
    print("Done.")
    print()
    return correction_factor


#uses sensor to calcualte the distance to an object
def getDistance():
    #TRIGGER THE SEONOR BY SETTING IT high for 
    # a short time and the nsetting it low
    GPIO.output(Trig, GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(Trig, GPIO.LOW)
    while(GPIO.input(Echo)==GPIO.LOW):
        start=time()
    while(GPIO.input(Echo)==GPIO.HIGH):
        end=time()
    duration=end-start

    distance=SPEED_OF_SOUND*duration

    distance/=2

    distance*=100
    return distance

########

#MAIN PROGRAM

#######
#first allow the sensor to settle for a bit
print("Wating for sensor to settle({}s".format(SETTLE_TIME))
GPIO.output(Trig, GPIO.LOW)
sleep(SETTLE_TIME) #seconds to let the sensor sett

#next calibrate the sensor
correction_factor=calibrate()
input("Press enter to begin...")
print("Getting Measurements")
while True:
    print("Measuring...")
    distance=getDistance()*correction_factor
    sleep(1)
    distance=round(distance,4)
    print("Distance measured: {cm}".format(distance))
    i=input("--Get another measurment (Y/n)? ")
    if (not i in [ "y", "Y", "yes", "yes", "" ]):
        break
#then measure
#finally  cleanup the GPIO pins 
print("Done.")
GPIO.cleanup()