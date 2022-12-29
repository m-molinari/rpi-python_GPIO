#! /usr/bin/env python3

# vim: set tabstop=4 shiftwidth=4 softtabstop=4 expandtab autoindent

"""
Simple script that looping 4 led blink
"""

import RPi.GPIO as GPIO
import time
import sys

# Setting up color/pin association
B = 17
R = 18
Y = 27
G = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup Pin
GPIO.setup(R, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(Y, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)

# Frequency to 100
r = GPIO.PWM(R, 100)
b = GPIO.PWM(B, 100)
y = GPIO.PWM(Y, 100)
g = GPIO.PWM(G, 100)
dc = 0

# Setting up list of colors
COLOR_LIST = [r, b, y, g]

while True:

    for COLOR in COLOR_LIST[:-1]:
        dc = 0 
        COLOR.start(dc)
    
        for x in range(3): 
            for i in range(0, 10): 
                dc += 10 
                # 0.0 <= dc <= 100.0
                COLOR.ChangeDutyCycle(dc)
                time.sleep(0.01) 
         
            for i in range(0, 10):
                dc -= 10 
                # 0.0 <= dc <= 100.0
                COLOR.ChangeDutyCycle(dc)
                time.sleep(0.01) 
        COLOR.stop() 
    
    COLOR_LIST.reverse()
    
    for COLOR in COLOR_LIST[:-1]:
        dc = 0
        COLOR.start(dc)
    
        for x in range(3):
            for i in range(0, 10):
                dc += 10
                # 0.0 <= dc <= 100.0
                COLOR.ChangeDutyCycle(dc)
                time.sleep(0.01)
    
            for i in range(0, 10):
                dc -= 10
                # 0.0 <= dc <= 100.0
                COLOR.ChangeDutyCycle(dc)
                time.sleep(0.01)
        COLOR.stop()

    COLOR_LIST.reverse()
