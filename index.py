import csv
import numpy as np

from fingerprint import fingerprint


def index_fingerprint(audio_file:str, song_name:str, artist_name:str):

    envelope = np.array(fingerprint(audio_file))

    with open('profiles2.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        field = [artist_name, song_name, envelope]
        writer.writerow(field)

    
   


index_fingerprint('./songs/Eminem.mp3','Lose yourself', 'Eminem')

index_fingerprint('./songs/StevieWonder.mp3','Part-Time Lover', 'Stevie Wonder')

index_fingerprint('./songs/TheWeeknd.mp3','Save Your Tears', 'The Weeknd')
