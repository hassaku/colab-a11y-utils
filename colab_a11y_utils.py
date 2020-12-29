from pydub import AudioSegment
from pydub.generators import Sine, Pulse, Square, Sawtooth, Triangle, WhiteNoise
from IPython.display import Audio, display
from tqdm.notebook import tqdm as original_tqdm


def speak(utterance):
    js = """
    <script>
    window.speechSynthesis.cancel();
    let msg = new SpeechSynthesisUtterance("%s");
    msg.lang = "en-US";
    window.speechSynthesis.speak(msg);
    </script>
    """ % utterance

    display(HTML(js))


class InvisibleAudio(Audio):
    def _repr_html_(self):
        audio = super()._repr_html_()
        audio = audio.replace('<audio', f'<audio onended="this.parentNode.removeChild(this)"')
        return f'<div style="display:none">{audio}</div>'


def __sound_notification_before(*args):
	sound = Triangle(440).to_audio_segment(duration=50).apply_gain(-10).fade_in(20).fade_out(20)
	display(InvisibleAudio(data=sound.export().read(), autoplay=True))


def __sound_notification_after(*args):
	sound = Triangle(440).to_audio_segment(duration=50).apply_gain(-10).fade_in(20).fade_out(20)
	sound += AudioSegment.silent(duration=100)
	sound += Triangle(440).to_audio_segment(duration=300).apply_gain(-10).fade_in(20).fade_out(20)
	display(InvisibleAudio(data=sound.export().read(), autoplay=True))


def __remove_callback(callback_name, function_name):
    ipython_events = get_ipython().events
    ipython_events.callbacks[callback_name] = list(
        filter(lambda fn: function_name not in repr(fn),
               ipython_events.callbacks[callback_name]))


def set_sound_notification():
    unset_sound_notification()
    ipython_events = get_ipython().events
    ipython_events.register('pre_run_cell', __sound_notification_before)
    ipython_events.register('post_run_cell', __sound_notification_after)


def unset_sound_notification():
    __remove_callback("pre_run_cell", "__sound_notification_before")
    __remove_callback("post_run_cell", "__sound_notification_after")



class tqdm(original_tqdm):
    def display(self, *args, **kwargs):
        progress_rate = self.n / self.total

		sound = Triangle(523.23 + progress_rate*523.27).to_audio_segment(duration=100)\
            .apply_gain(-10)\
            .fade_in(20)\
            .fade_out(20)\
            .pan(-1.0 + progress_rate * 2)

        display(InvisibleAudio(data=sound.export().read(), autoplay=True))

        super(tqdm, self).display(*args, **kwargs)

