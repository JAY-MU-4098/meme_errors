# Meme Errors



Play funny meme sounds whenever Python exceptions occur — **even if the error is handled!** Customize your sounds per exception type, set trim duration, and enjoy some chaotic developer humor. 

### Features
*   **Automatic memes** on uncaught exceptions.
*   **Handled exceptions support** via decorator or context manager.
*   **Custom sounds** per exception type.
*   **Automatic trimming** of long sounds (default 3 seconds).
*   **Optional custom duration** per error or decorator.

---

## Installation

```bash
pip install meme-errors
```

Use code with caution. Usage Global Uncaught Errors Automatically plays a meme when an exception occurs that is not handled:
```
import meme_errors

# This will play the default Exception meme
1 / 0  # Division by zero
```


Custom Memes for Specific Exceptions
```
import meme_errors

# Set a custom meme for TypeError
meme_errors.set_error_sound(TypeError, "/path/to/emotional-damage-meme.mp3")

# Set a custom meme for FileNotFoundError
meme_errors.set_error_sound(FileNotFoundError, "/path/to/galaxy-meme.mp3")
```

Handled Exceptions Using a Decorator 
```
from meme_errors import meme_sound_on_error

@meme_sound_on_error
def risky_func():
    try:
        open("missing_file.txt")  # FileNotFoundError
    except FileNotFoundError:
        print("Caught the error, but meme still plays!")

risky_func()
```

Custom Duration for Decorator
```
# Set duration to 5 seconds
risky_func = meme_sound_on_error(risky_func, duration_ms=5000) 
```
Manual Meme Playback

```
from meme_errors import play_meme_sound

# Play TypeError meme for default 3 seconds
play_meme_sound(TypeError)

# Play TypeError meme for 5 seconds
play_meme_sound(TypeError, duration_ms=5000)
```
Default Memes Included:

| Exception Type        | Default Meme File                      |
|-----------------------|----------------------------------------|
| TypeError             | emotional-damage-meme.mp3              |
| FileNotFoundError     | galaxy-meme.mp3                        |
| Exception (fallback)  | meme-de-creditos-finales.mp3           |

You can replace these using `set_error_sound()`.

## Notes:

- **Audio Trimming:** Audio is trimmed to a default of 3 seconds to prevent long playback.  
- **Compatibility:** Works on Windows, macOS, and Linux (requires `playsound` and `pydub`).  
- **Non-blocking:** Playback is handled via `playsound`.  

## License:

MIT License – see [LICENSE](LICENSE) file.  

## Contributing:

Fork the repo, add your own meme sounds or improve features, and submit a Pull Request.  
Have fun making Python errors **hilarious!** 😂