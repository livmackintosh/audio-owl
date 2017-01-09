#!/usr/bin/env python3

import math
from mpd import MPDClient

class OwlyPlayer():
    
    FADE_PERIOD = 30 # Number of seconds to fade over.
     
    def __init__(self):
        self.client = MPDClient()
        self.client.timeout = 30
        self.client.idletimeout = None
        self.client.connect("localhost", 6600)

    def ramp_up(self, time):
        return ((math.sin((time * math.pi) / (30 * self.FADE_PERIOD) - math.pi/2)+1)/2)

    def ramp_down(self, time):
        return -((math.sin((time * math.pi) / (30 * self.FADE_PERIOD) + math.pi/2)+1)/2)+1
    
    def test(self):
        print(self.client.status())

