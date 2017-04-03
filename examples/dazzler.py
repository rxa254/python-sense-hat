#!/usr/bin/python
from __future__ import division
import time, sys, signal

import numpy as np

from sense_hat import SenseHat

sense = SenseHat()

# initial startup color
r = 111
g = 55
b = 22

# do a sleep in units of milli-seconds
def msleep(sleep_time_ms):
        time.sleep(sleep_time_ms / 1000)

# catch the CTRL-C and die gracefully
def sigint_handler(signum, frame):
        print('\n')
        print('CTRL-C Encountered...Shutting down.\n')
        sense.clear([0,0,0])
        sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)
        

def next_colour(r,g,b):

    r,g,b = np.random.random_integers(0, 255, size=(3,1))
    
    return r,g,b

# this is the main loop
mmm = 0
while mmm < 1e3:
        sense.clear([r, g, b])
        msleep(111)
        r,g,b = next_colour(r,g,b)
        mmm += 1
