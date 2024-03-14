import csv
import numpy as np

from fingerprint import fingerprint


def index_fingerprint(audio_file, song_name, artist_name):

    envelope = np.array(fingerprint(audio_file))

    with open('profiles2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["artist_name", "song_name", "envelope"]
        writer.writerow(field)
   


index_fingerprint(./Eminem.mp3, Lose yourself, artist_name)