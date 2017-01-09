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
        Gtk.Window.__init__(self, title="Audio-Owl Dev")
        self.set_border_width(10) 
        Gtk.Orientation

        # Create a box to pack our widgets
        self.box = Gtk.Box(spacing=6)
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # Create the current file label
        self.current_file=Gtk.Label()
        self.box.pack_start(self.current_file, True, True, 0)

        # Create the file-picker and event handler
        self.choose_audio_btn=Gtk.Button(label="Load Audio")
        self.choose_audio_btn.connect("clicked", self.choose_audio)
        self.box.pack_start(self.choose_audio_btn, True, True, 0)

        # Create the play button and event handler
        self.play_audio_btn=Gtk.Button(label="Play Audio")
        self.play_audio_btn.connect("clicked", self.play_audio)
        self.box.pack_start(self.play_audio_btn, True, True, 0)


    def choose_audio(self, widget):
        """Opens a load file chooser dialog"""
        dialog = Gtk.FileChooserDialog("Pick an audio file", self, 
            Gtk.FileChooserAction.OPEN, 
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_file_filters(dialog)
        
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("File open successful")
        elif response == Gtk.ResponseType.CANCEL:
            print("File open cancelled")
        self.current_file.set_text(dialog.get_filename())
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
        
win = OwlyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
