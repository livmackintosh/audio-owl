#!/usr/bin/env python3
"""Audio-Owl - A very relaxing audio player.

   player - AudioOwl Player

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

from vlc import MediaPlayer

from . import volume


class OwlyPlayer(MediaPlayer):
    """An audio player class that uses some rather relaxing methods"""
    def __init__(self):
        MediaPlayer.__init__(self)
        self.volcalc = volume.envelope(fade, length)

    def start_sleepy(self):
        """Start the sleepy routine."""
        while self.is_playing():
            self.audio_set_volume(self.volcalc(self.get_time()))

            # Print diagnostic information
            log("DEBUG", "OwlyWindow", "Current Volume {}"
                .format(self.audio_get_volume()))
            log("DEBUG", "OwlyWindow", "Current Time   {}"
                .format(self.get_time() / 999))
