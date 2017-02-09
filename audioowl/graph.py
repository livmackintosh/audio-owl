#!/usr/bin/env python3
"""Audio-Owl - A very relaxing audio player.

   graph - Generates and displays graphs relating to audioowl

   Copyright (C) 2016  Olivia Mackintosh

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import matplotlib.pyplot as graph
import pylab

from .player import volume

FADE_PERIOD = 30  # Number of milliseconds to fade over.
AUDIO_LENGTH = 181  # Number of milliseconds of total audio length to graph.

vol_calc = volume.envelope(FADE_PERIOD, AUDIO_LENGTH)

xvalues = list(range(AUDIO_LENGTH))
yvalues = list(map(vol_calc, xvalues))
graph.plot(xvalues, yvalues)
graph.title("Volume Envalope")
graph.xlabel("Audio Progress (s)")
graph.ylabel("Volume (%)")
graph.yscale("log")
graph.grid(True)
if __name__ == '__main__':
    pylab.show()
