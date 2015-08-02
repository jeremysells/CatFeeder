# Copyright (c) 2015 Jeremy Sells
# For copying permission, copyright information, terms, etc read the
# LICENSE (file) that that was distributed with this source code.
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

# Loop 1 - Clear the switches true state
print "Loop 1"
loop1 = True
while loop1:
    if (GPIO.input(MororSwitch) == True):
        loop1 = False
    sleep(0.01)

# Loop 2 - Loop until the switch is set
print "Loop 2"
loop2 = True
while loop2:
    if (GPIO.input(MororSwitch) == False):
        loop2 = False
    sleep(0.01)

# We have dished out food, stop the motor
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)

# Cleanup
GPIO.cleanup()