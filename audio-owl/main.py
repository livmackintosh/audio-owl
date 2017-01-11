#!/usr/bin/env python
"""Audio-Owl
   A very relaxing audio player.
   Copyright (c) 2016 Olivia Mackintosh <livvy@base.nu>
"""

import gi
gi.require_version('Gtk', '3.0') # Use GTK3+
from gi.repository import Gtk

from mpd import MPDClient


""" Main Window """
class OwlyWindow(Gtk.Window):
  
    def __init__ (self):
        # Initialize the OwlyWindow
        self.builder = Gtk.Builder()
        self.builder.add_from_file("owlywindow.glade")
        self.builder.connect_signals(self)

    def choose_audio(self, widget):
        """Opens a load file chooser dialog"""
        
        print("Handler Executed")
        
        dialog = self.builder.get_object("song_picker_dlg")
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("File open successful")
        elif response == Gtk.ResponseType.CANCEL:
            print("File open cancelled")
        
        widget.set_text(dialog.get_filename())
        dialog.destroy()

    def add_file_filters(self, dialog):
        filter_audio = Gtk.FileFilter()
        filter_audio.set_name("Audio Files")
        filter_audio.add_mime_type("audio/ogg")
        filter_audio.add_mime_type("audio/mp3")
        dialog.add_filter(filter_audio)


    def play_audio(self, widget):
        """Plays the current file via MPD"""
        self.mpd_client = MPDClient()
        self.mpd_client.connect("/home/livvy/.mpd/socket", 0)
        self.mpd_client.clear()
        self.mpd_client.add(self.current_file.get_text())
        self.mpd_client.play(0)

ow = OwlyWindow()
win = ow.builder.get_object("owly_window")
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
