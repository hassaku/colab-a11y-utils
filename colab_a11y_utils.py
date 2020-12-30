from pydub import AudioSegment
from pydub.generators import Sine, Pulse, Square, Sawtooth, Triangle, WhiteNoise
from IPython.display import Audio, display
from tqdm.notebook import tqdm as original_tqdm
from IPython.core.ultratb import AutoFormattedTB
from IPython.display import HTML, display


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
    sound = Triangle(440).to_audio_segment(duration=50).apply_gain(-20).fade_in(20).fade_out(20)
    sound += AudioSegment.silent(duration=100)
    display(InvisibleAudio(data=sound.export().read(), autoplay=True))


def __sound_notification_success(*args):
    HZ = 540
    sound = Triangle(HZ).to_audio_segment(duration=100).apply_gain(-20).fade_in(20).fade_out(20)
    sound += AudioSegment.silent(duration=100)
    sound += Triangle(HZ).to_audio_segment(duration=100).apply_gain(-20).fade_in(20).fade_out(20)
    display(InvisibleAudio(data=sound.export().read(), autoplay=True))


def __sound_notification_error(*args):
    HZ = 100
    sound = Sawtooth(HZ).to_audio_segment(duration=100).apply_gain(-20).fade_in(20).fade_out(20)
    sound += AudioSegment.silent(duration=100)
    sound += Sawtooth(HZ).to_audio_segment(duration=100).apply_gain(-20).fade_in(20).fade_out(20)
    display(InvisibleAudio(data=sound.export().read(), autoplay=True))


def __sound_notification_after(*args):
    __sound_notification_success()


def __remove_callback(callback_name, function_name):
    ipython_events = get_ipython().events
    ipython_events.callbacks[callback_name] = list(
        filter(lambda fn: function_name not in repr(fn),
               ipython_events.callbacks[callback_name]))


def __sound_error(shell, etype, evalue, tb, tb_offset=None):
    shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
    __sound_notification_error()


def __silent_error(shell, etype, evalue, tb, tb_offset=None):
    shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)


def unset_sound_notifications():
    __remove_callback("pre_run_cell", "__sound_notification_before")
    __remove_callback("post_run_cell", "__sound_notification_after")
    get_ipython().set_custom_exc((Exception,), __silent_error)


def set_sound_notifications():
    unset_sound_notifications()
    ipython_events = get_ipython().events
    ipython_events.register('pre_run_cell', __sound_notification_before)
    ipython_events.register('post_run_cell', __sound_notification_after)
    get_ipython().set_custom_exc((Exception,), __sound_error)


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

