
import threading


class UpdateProgress(threading.Thread):
    def run(self):
        """Continuously updates the progress bar until it reaches 1.0 (100%).
        This should be called in a thread so it doesn't block anything. This
        should exit once the song has finished playing.
        """
        pb = self.main.get_object('progress_bar')
        while self.player.is_playing():
            sleep(0.1)
            pb.set_fraction(self.player.get_position())
