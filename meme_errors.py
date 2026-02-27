import sys
from pathlib import Path
from playsound import playsound
from pydub import AudioSegment

# Default meme sounds
DEFAULT_SOUNDS = {
    "TypeError": "sounds/emotional-damage-meme.mp3",
    "FileNotFoundError": "sounds/galaxy-meme.mp3",
    "Exception": "sounds/movie_1_C2K5NH0.mp3"  # fallback
}

# Default trim duration in milliseconds
DEFAULT_DURATION_MS = 3000  # 3 sec

# Play sound with optional duration (ms)
def play_meme_sound(exc_type, duration_ms=DEFAULT_DURATION_MS):
    sound_file = DEFAULT_SOUNDS.get(exc_type.__name__, DEFAULT_SOUNDS["Exception"])
    path = Path(__file__).parent / sound_file
    try:
        audio = AudioSegment.from_file(path)
        if len(audio) > duration_ms:
            audio = audio[:duration_ms]  # trim to duration
        # Export trimmed temp file
        temp_path = Path(__file__).parent / "temp_trimmed.mp3"
        audio.export(temp_path, format="mp3")
        playsound(str(temp_path))
    except Exception as e:
        print(f"[Meme Errors] Failed to play sound: {e}")

# Global exception hook
def meme_excepthook(exc_type, exc_value, traceback):
    play_meme_sound(exc_type)
    sys.__excepthook__(exc_type, exc_value, traceback)

sys.excepthook = meme_excepthook

# Add or change meme for an error type
def set_error_sound(exc_type, mp3_path):
    path = Path(mp3_path)
    if not path.exists():
        raise FileNotFoundError(f"{mp3_path} does not exist!")

    DEFAULT_SOUNDS[exc_type.__name__] = str(path)

# Decorator for function-level errors
def meme_sound_on_error(func, duration_ms=DEFAULT_DURATION_MS):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            play_meme_sound(type(e), duration_ms)
            raise e
    return wrapper