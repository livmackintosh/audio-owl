from audioowl.player import volume


class TestIncreasingEnvelope():

    def test_start(self):
        """Volume should be 0% at the start of the fade-in"""
        assert volume.increasing(30)(0) == 0.0

    def test_mid(self):
        """Volume should be 50% when the fade-in is halfway"""
        assert round(volume.increasing(30)(15), 2) == 0.5

    def test_end(self):
        """Volume should be 100% when the fade-in has ended"""
        assert volume.increasing(30)(30) == 1.0


class TestDecreasingEnvelope():

    def test_start(self):
        """Volume should be 100% at the start of the fade-out"""
        assert volume.decreasing(30)(0) == 1.0

    def test_mid(self):
        """Volume should be 50% when the fade-out is halfway"""
        assert round(volume.decreasing(30)(15), 2) == 0.5

    def test_env(self):
        """Volume should be 0% when the fade-out has ended"""
        assert volume.decreasing(30)(30) == 0.0
