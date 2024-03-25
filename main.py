import librosa
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from Constellation_map import compute_spectrogram, plot_constellation_map, constellation_map
from Comparison import is_same_sound_db

csv_file = 'profiles2.csv'

# record files
filename = "songs/bakermat.mp3"
filename2 = "songs/record1.mp3"
filename3 = "songs/record1.mp3"
filename4 = "songs/record1.mp3"

# read this file 


# compute spectrogram of record file
Y = compute_spectrogram(filename)

# constellation
Cmap_record = constellation_map(Y)
fig, ax, im = plot_constellation_map(Cmap_record, Y=Y)
plt.show()

# parcourir 

# Ouvrir le fichier CSV en mode lecture
with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:  # Ensure the row has at least three elements
                artist_name = row[0]
                song_name = row[1]
                constellation_str = row[2]
                # comparison with dataset
                same_sound = is_same_sound_db(Cmap_record,constellation_str)
                if same_sound==True:
                    print("C'est la même musique que " , song_name," de ", artist_name)
                    break
if same_sound == False:
        print("Pas d'artiste trouvé...")


# plot the 2 chromagram in the same graph


# is a music find

    # output music

# else : add to the dataset 
 