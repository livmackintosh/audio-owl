#!/usr/bin/env python
"""Audio-Owl
   Plays audio files and streams according to a timed schedule.
   Olivia Mackintosh <livvy@base.nu>
"""

import gi
gi.require_version('Gtk', '3.0') # Use GTK3+
from gi.repository import Gtk

""" Main Window """

class OwlyWindow(Gtk.Window):
    
    audio_file = None

    def __init__ (self):
        Gtk.Window.__init__(self, title="Audio-Owl")

        self.choose_audio_btn=Gtk.Button(label="Load Audio")
        self.choose_audio_btn.connect("clicked", self.choose_audio)
        self.add(self.choose_audio_btn)

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
        self.audio_file = dialog.get_filename()
        dialog.destroy()

    def add_file_filters(self, dialog):
        filter_audio = Gtk.FileFilter()
        filter_audio.set_name("Audio Files")
        filter_audio.add_mime_type("audio/ogg")
        filter_audio.add_mime_type("audio/mp3")
        dialog.add_filter(filter_audio)

win = OwlyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
