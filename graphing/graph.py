#!/usr/bin/env python

import matplotlib.pyplot as plt
import pylab
import math

FADE_PERIOD  = 30 # Number of milliseconds to fade over.
AUDIO_LENGTH = 90 # Number of milliseconds of total audio length to graph.

def ramp_up(t):
    return ((math.sin((t * math.pi) / (FADE_PERIOD*1000) - math.pi/2)+1)/2)

def ramp_dn(t):
    return ((math.sin((t * math.pi) / (FADE_PERIOD*1000) + math.pi/2)+1)/2)

ramp_up_x_series = list(range(1,FADE_PERIOD*1000-1))
ramp_cn_x_series = list(range(ramp_up_x_series[-1]+1, AUDIO_LENGTH*1000-(FADE_PERIOD*1000)-1))
ramp_dn_x_series = list(range(ramp_cn_x_series[-1]+1, AUDIO_LENGTH*1000))

x_series = ramp_up_x_series + ramp_cn_x_series + ramp_dn_x_series

ramp_up_y_series = list(map(ramp_up, ramp_up_x_series))
ramp_cn_y_series = [1.0] * len(ramp_cn_x_series)
ramp_dn_y_series = list(map(ramp_dn, ramp_dn_x_series))

y_series = ramp_up_y_series + ramp_cn_y_series + ramp_dn_y_series

plt.plot(x_series, y_series)
pylab.show()
