"""Audio-Owl - A very relaxing audio player.

   This is the volume module of audioowl. It contains the mathematical
   functions that describe the volume of the audio at a given moment.

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

from typeguard import typechecked
from math import sin, pi


@typechecked
def increasing(fade: int):
    """Returns a function that defines an increasing volume envelope"""
    return lambda t: ((sin((t * pi) / (fade) - pi / 2) + 1) / 2)


@typechecked
def decreasing(fade: int):
    """Returns a function that defines a decreasing volume envelope"""
    return lambda t: ((sin((t * pi) / (fade) + pi / 2) + 1) / 2)


@typechecked
def envelope(fade: int, length: int):
    """Returns a function based on the fade time and length of the song that
       takes the current time and returns the volume as a percentage"""
    def calculator(t):
        if t < fade:
            return increasing(fade)(t)
        elif (length - fade) < t:
            return decreasing(fade)(length + fade - t)
        else:
            return 1.0
    return calculator
