#!/usr/bin/env python3
"""Audio-Owl - A very relaxing audio player.

   gui - Audio-Owl GUI

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

import math
import gi
import logging
import vlc
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future

from . import player

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

LOG_DEBUG = True


class OwlyWindow(Gtk.ApplicationWindow):
    """A window class that provides audio-owl widgets and event handlers to
    provide a graphical user interface for AudioOwl
    """

    FADE_PERIOD = 30  # Number of seconds to fade over
    filename = None

    def __init__(self):
        self.executor = ThreadPoolExecutor()
        self.main = self.builder()
        self.start_stop_btn = self.main.get_object('start_stop_btn')
        self.player = player.OwlyPlayer()
        logging.info("Successfully initialized OwlyWindow")

    def builder(self):
        """Returns a new window builder instance"""
        builder = Gtk.Builder()
        builder.add_from_file("assets/owlywindow.glade")
        builder.connect_signals(self)
        return builder

    def on_load_song_btn_clicked(self, widget):
        """Opens a load file chooser dialog and sets the current filename if the
        song picking was successful."""
        logging.info("Load song button clicked. Displaying dialog.")
        dialog = self.builder().get_object("song_picker_dialog")
        dialog.set_transient_for(self.builder().get_object("main_window"))
        response = dialog.run()
        if response == 1:
            self.filename = dialog.get_filename()
            if self.filename is not None:
                self.main.get_object(
                    "current_song_content_lbl").set_text(self.filename)
        dialog.destroy()

    def on_start_stop_btn_clicked(self, widget):
        """Starts and stops audio-owl from playing"""

        logging.info("Start/Stop Button Activated")

        if self.player.is_playing():

            self.player.stop()
            self.start_stop_btn.set_label("Start Playing")
            logging.info("Stopped Playing")

        elif self.filename is not None:
            self.start_stop_btn.set_label("Stop Playing")
            self.player.set_media(vlc.Media(self.filename))
            self.FADE_PERIOD = self.main.get_object(
                'fade_period_spinbtn').get_value_as_int()
            # Make sure volume is 0% and start playing
            self.player.audio_set_volume(0)
            sleep(0.5)
            self.player.play()
            sleep(0.5)  # Avoid some weird race condition
            self.sr = self.executor.submit(self.player.start_sleepy)
            self.up = self.executor.submit(self.update_progress)
            logging.info("Started Playing")

    def open_about_dialog(self, widget):
        self.builder().get_object("about_dialog").run()

    def update_progress(self):
        """Continuously updates the progress bar until it reaches 1.0 (100%).
        This should be called in a thread so it doesn't block anything. This
        should exit once the song has finished playing.
        """
        pb = self.main.get_object('progress_bar')
        while self.player.is_playing():
            sleep(0.1)
            pb.set_fraction(self.player.get_position())

    def quit(self, *args, **kwargs):
        """Stop the audio, kill the threads and kill Gtk.main()
        """
        self.player.stop()
        self.executor.shutdown()
        Gtk.main_quit()
        logging.info("Quitting.")

def run():
    ow = OwlyWindow()
    win = ow.main.get_object("main_window")
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
