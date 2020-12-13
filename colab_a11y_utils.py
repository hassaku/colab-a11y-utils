from pydub import AudioSegment
from pydub.generators import Sine, Pulse, Square, Sawtooth, Triangle, WhiteNoise
from IPython.display import Audio, display

from tqdm.notebook import tqdm as original_tqdm


class InvisibleAudio(Audio):
    def _repr_html_(self):
        audio = super()._repr_html_()
        audio = audio.replace('<audio', f'<audio onended="this.parentNode.removeChild(this)"')
        return f'<div style="display:none">{audio}</div>'


def set_sound_notification():
    def sound_notification_before(*args):
        sound = Triangle(440).to_audio_segment(duration=50).apply_gain(-10).fade_in(20).fade_out(20)
        display(InvisibleAudio(data=sound.export().read(), autoplay=True))

    def sound_notification_after(*args):
        sound = Triangle(440).to_audio_segment(duration=50).apply_gain(-10).fade_in(20).fade_out(20)
        sound += AudioSegment.silent(duration=100)
        sound += Triangle(440).to_audio_segment(duration=300).apply_gain(-10).fade_in(20).fade_out(20)
        display(InvisibleAudio(data=sound.export().read(), autoplay=True))

    get_ipython().events.register('pre_run_cell', sound_notification_before)
    get_ipython().events.register('post_run_cell', sound_notification_after)



class tqdm(original_tqdm):
    def display(self, *args, **kwargs):
        progress_rate = self.n / self.total

        sound = Triangle(523.23 + progress_rate*523.27).to_audio_segment(duration=100).apply_gain(-10).fade_in(20).fade_out(20)
        display(InvisibleAudio(data=sound.export().read(), autoplay=True))

        super(tqdm, self).display(*args, **kwargs)

