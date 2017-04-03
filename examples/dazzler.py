#!/usr/bin/python
from __future__ import division
import time, sys, signal
import argparse

import numpy as np

from sense_hat import SenseHat

parser = argparse.ArgumentParser(description='Randomly Flash the LEDs.')
parser.add_argument('refresh_period', metavar='tau', type=float,
                    help='LED Refresh Period [ms]')
args = parser.parse_args()

tau = args.refresh_period

sense = SenseHat()


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
        
# the function that determines the color matrix
def next_color(pixels):

        #length,width = pixels.shape
        #pix = np.random.randint(-33, 33, size=(length, width))
        pix = np.random.standard_normal(pixels.shape)
        pix = np.floor(10*pix)
        pix = pixels + pix.astype(int)
        pix = np.clip(pix, 0, 255)

        return pix

# initial startup color
pixels = np.random.random_integers(0, 255, size=(64, 3))
sense.set_pixels(pixels)

# this is the main loop
mmm = 0
while mmm < 1e6: #set up a counter so it doesn't go on forever

        pixels = next_color(pixels)
        sense.set_pixels(pixels)
        msleep(tau)
        mmm += 1

sense.clear()
