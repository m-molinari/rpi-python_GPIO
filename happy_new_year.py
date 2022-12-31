#! /usr/bin/env python3

# vim: set tabstop=4 shiftwidth=4 softtabstop=4 expandtab autoindent

import RPi.GPIO as GPIO
import time
import sys

# Setting up color/pin association
R = 18
B = 17
Y = 27
G = 22
W = 23
R1 = 24
B1 = 25
Y1 = 8
G1 = 7
W1 = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup Pin
GPIO.setup(R, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(Y, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(W, GPIO.OUT)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(Y1, GPIO.OUT)
GPIO.setup(G1, GPIO.OUT)
GPIO.setup(W1, GPIO.OUT)

COLOR_LIST = [R,B,Y,G,W,R1,B1,Y1,G1,W1]

def start_blink(N):
    print("Starting: " + start_blink.__name__)
    START_BLINK_LIST = [R, B, Y, G, W, R1, B1, Y1, G1, W1 ] 
    for k in range(N):
        for COLOR in START_BLINK_LIST:
            GPIO.output(COLOR, True)
        time.sleep(0.5)
        for COLOR in START_BLINK_LIST:
            GPIO.output(COLOR, False)
        time.sleep(0.5)

def same_color(N):
    print("Starting: " + same_color.__name__)
    SAME_COLOR_LIST = [R, R1, B, B1, Y, Y1,G, G1, W, W1]
    for k in range(N):
        for COLOR in SAME_COLOR_LIST:
            GPIO.output(COLOR, True)
            time.sleep(0.1)
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, False)
        time.sleep(000.2)

def edge(N):
    print("Starting: " + edge.__name__)
    EDGE_LIST = [R, W1, B, G1, Y, Y1, G, B1, W, R1] 
    for k in range(N):
        for COLOR in EDGE_LIST:
            GPIO.output(COLOR, True)
            time.sleep(0.08)
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, False)

def snake(N):
    print("Starting: " + snake.__name__)
    for k in range(2):
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, True)
            time.sleep(0.08)
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, False)
            time.sleep(0.08)
        COLOR_LIST.reverse()
    
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, True)
            time.sleep(0.08)
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, False)
            time.sleep(0.08)
        COLOR_LIST.reverse()

def center_to_edge(N):
    print("Starting: " + center_to_edge.__name__)
    CENTER_TO_EDGE_LIST = [R1, W, B1, G, Y1, Y, G1, B, W1, R ] 
    for k in range(N):
        for COLOR in CENTER_TO_EDGE_LIST:
            GPIO.output(COLOR, True)
            time.sleep(0.08)
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, False)

def all_on(N):
    print("Starting: " + all_on.__name__)
    ALL_ON_LIST = [R, W1, B, G1, Y, Y1, G, B1, W, R1 ]
    for k in range(N):
        for COLOR in ALL_ON_LIST:
            GPIO.output(COLOR, True)
        time.sleep(0.08)
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, False)
            time.sleep(0.08)

def wave(N):
    print("Starting: " + wave.__name__)
    for k in range(N):
        GPIO.output(R1, True)
        GPIO.output(W, True)
        time.sleep(0.1)
        GPIO.output(B1, True)
        GPIO.output(G, True)
        time.sleep(0.1)
        GPIO.output(Y1, True)
        GPIO.output(Y, True)
        time.sleep(0.1)
        GPIO.output(G1, True)
        GPIO.output(B, True)
        time.sleep(0.1)
        GPIO.output(W1, True)
        GPIO.output(R, True)
        time.sleep(0.1)
        GPIO.output(R1, False)
        GPIO.output(W, False)
        time.sleep(0.1)
        GPIO.output(B1, False)
        GPIO.output(G, False)
        time.sleep(0.1)
        GPIO.output(Y1, False)
        GPIO.output(Y, False)
        time.sleep(0.1)
        GPIO.output(G1, False)
        GPIO.output(B, False)
        time.sleep(0.1)
        GPIO.output(W1, False)
        GPIO.output(R, False)

def sequential(N):
    print("Starting: " + sequential.__name__)
    for k in range(N):
        for COLOR in COLOR_LIST:
            GPIO.output(COLOR, True)
            time.sleep(0.04)
            GPIO.output(COLOR, False)

def main():
    start_blink(2)  
    same_color(4)
    edge(4)
    snake(4)
    center_to_edge(4)
    all_on(2)
    wave(2)
    sequential(8)
    GPIO.cleanup()

if __name__ == '__main__':

  try:
    main()

  except :
      print('Something went wrong !')

