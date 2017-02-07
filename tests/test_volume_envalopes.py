import pytest
import audio_owl

ow = audio-owl.OwlyWindow()

class TestVolumeEnvalopes():

def test_ramp_up_start():
    assert ow.ramp_up(0) == 0

def test_ramp_up_end():
    assert ow.ramp_up(30) == 1
