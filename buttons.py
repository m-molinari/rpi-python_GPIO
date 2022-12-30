#! /usr/bin/env python3

# vim: set tabstop=4 shiftwidth=4 softtabstop=4 expandtab autoindent

import random
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 18
yellow = 27
green = 22
blue = 17

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    redButtonState = GPIO.input(12)
    if redButtonState == 0:
        GPIO.output(red, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(red, GPIO.LOW)
    blueButtonState = GPIO.input(16)

    if blueButtonState == 0:
        GPIO.output(blue, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(blue, GPIO.LOW)
    yellowButtonState = GPIO.input(20)

    if yellowButtonState == 0:
        GPIO.output(yellow, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(yellow, GPIO.LOW)
    greenButtonState = GPIO.input(21)

    if greenButtonState == 0:
        GPIO.output(green, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(green, GPIO.LOW)

