# Copyright (c) 2015 Jeremy Sells
# For copying permission, copyright information, terms, etc read the
# LICENSE (file) that that was distributed with this source code.

# The page (below) was very helpful when writing this script
# http://computers.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051

# Infinate loop - useful for debugging
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# Define GPIO PINS
Motor1A = 16
Motor1B = 18
Motor1E = 22
MororSwitch = 11;

# Setup pins
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(MororSwitch,GPIO.IN)

# Turn motor on
print "Turning motor on"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

# Infinate Loop
print "Looping forever"
while True:
    print "switch state = " + str(GPIO.input(MororSwitch))

# We should never get here
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)

# Cleanup
GPIO.cleanup()
