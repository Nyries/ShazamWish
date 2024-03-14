import librosa
import numpy as np
import sounddevice as sd
import sys


def play_sound(filename):
    y, sr = librosa.load(filename, sr=None)
    # Start playing the sound
    sd.play(y, sr)

    # Keep checking for user input to stop the sound
    print("Press 'Enter' to stop the sound.")
    input()
    # Stop the sound
    sd.stop()


if __name__ == "__main__":
    filename = "sound/music.mp3"
    play_sound(filename)




