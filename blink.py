#! /usr/bin/env python3

# vim: set tabstop=4 shiftwidth=4 softtabstop=4 expandtab autoindent

import RPi.GPIO as GPIO
import time
import sys

# Setting up color/pin association
B = 17
R = 18
Y = 22
G = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup Pin
GPIO.setup(R, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(Y, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)

while True:
    GPIO.output(R, True)
    time.sleep(00000.1)
    GPIO.output(R, False)
    time.sleep(00000.1)
    
    GPIO.output(B, True)
    time.sleep(00000.1)
    GPIO.output(B, False)
    time.sleep(00000.1)
    
    GPIO.output(G, True)
    time.sleep(00000.1)
    GPIO.output(G, False)
    time.sleep(00000.1)
    
    GPIO.output(Y, True)
    time.sleep(00000.1)
    GPIO.output(Y, False)
    time.sleep(00000.1)

GPIO.cleanup()
