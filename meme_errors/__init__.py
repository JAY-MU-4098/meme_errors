import sys
from pathlib import Path

import pygame
import importlib.resources as resources
from . import sounds

# Initialize pygame mixer once
pygame.mixer.init()

DEFAULT_SOUNDS = {
    "TypeError": "emotional-damage-meme.mp3",
    "FileNotFoundError": "galaxy-meme.mp3",
    "Exception": "movie_1_C2K5NH0.mp3"
}


def play_meme_sound(exc_type):
    # Get sound file based on exception name
    sound_file = DEFAULT_SOUNDS.get(exc_type.__name__, DEFAULT_SOUNDS["Exception"])
    try:
        # Get path directly from package resources
        traversable = resources.files(sounds).joinpath(sound_file)

        with resources.as_file(traversable) as path:
            pygame.mixer.music.load(str(path))
            pygame.mixer.music.play()

            # This loop waits for the sound to finish
            # To limit to 3 seconds, you can add a counter here
            start_time = pygame.time.get_ticks()
            while pygame.mixer.music.get_busy():
                # Stop if it exceeds 3 seconds (3000ms)
                if pygame.time.get_ticks() - start_time > 3000:
                    pygame.mixer.music.stop()
                    break
                pygame.time.Clock().tick(10)

    except Exception as e:
        # Silently fail so we don't cause an error during an error
        pass


def meme_excepthook(exc_type, exc_value, traceback):
    play_meme_sound(exc_type)
    sys.__excepthook__(exc_type, exc_value, traceback)


# Global hook
sys.excepthook = meme_excepthook


# Decorator for function-level errors
def meme_sound_on_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            play_meme_sound(type(e))
            raise e

    return wrapper

def set_error_sound(exc_type, mp3_path):
    """Allows users to map a custom .mp3 to an error type"""
    path = Path(mp3_path)
    if not path.exists():
        raise FileNotFoundError(f"{mp3_path} does not exist!")
    # Store the absolute path string in the dictionary
    DEFAULT_SOUNDS[exc_type.__name__] = str(path.absolute())
