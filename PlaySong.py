import librosa
import numpy as np
import sounddevice as sd


filename = "music.mp3"


y, sr = librosa.load(filename, sr = None)
sd.play(y,sr)
sd.wait()


