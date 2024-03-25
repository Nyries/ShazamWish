import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.feature import peak_local_max
from profiles2 import *

# Load a short recording with some background noise
filename = "sound/music.mp3"
y, sr = librosa.load(librosa.ex('recording'),offset=30, duration=10)
# Create the constellation and hashes
constellation = constellation(audio_input, Fs)
hashes = create_hashes(constellation, None)

# For each hash in the song, check if there's a match in the database
# There could be multiple matches, so for each match:
#   Append all of them to a hashmap based on the song id along with the time
#   the hash occurs in the sample and at the source
# In the end, matches_per_song is key'd by song ID with values being
# lists of hashes, the 
matches_per_song = {}
for hash, (sample_time, _) in hashes.items():
    if hash in profiles2:
        matching_occurences = database[hash]
        for source_time, song_id in matching_occurences:
            if song_id not in matches_per_song:
                matches_per_song[song_id] = []
            matches_per_song[song_id].append((hash, sample_time, source_time))