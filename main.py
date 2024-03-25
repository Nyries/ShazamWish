import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from Constellation_map import compute_spectrogram, plot_constellation_map
from Comparison import is_same_sound
import csv

csv_file_path = "profiles2.csv"


# record files
filename = "songs/record1.mp3"
filename2 = "songs/record1.mp3"
filename3 = "songs/record1.mp3"
filename4 = "songs/record1.mp3"

# read this file 



# compute spectrogram of record file
Y = compute_spectrogram(filename ,N=2048,H=2048,Fs=22050,bin_max=128,frame_max=1000)

# constellation
fig, ax, im = plot_constellation_map(Cmap, Y=None, xlim=None, ylim=None, title='',xlabel='Time (sample)', ylabel='Frequency (bins)',s=5, color='r', marker='o', figsize=(7, 3), dpi=72):

# parcourir 


# Ouvrir le fichier CSV en mode lecture
with open(csv_file_path, newline='') as csvfile:
    # Lire le fichier CSV
    csv_reader = csv.reader(csvfile)
    # Parcourir chaque ligne du fichier CSV
    for row in csv_reader: 
        # comparison
        is_same_sound(filename,filename2,dist_freq=15, dist_time=15,thresh=0.7,tol_freq=5, tol_time=5)

# chose the reliability percentage


# comparison with dataset


# plot the 2 chromagram in the same graph


# is a music find

    # output music

# else : add to the dataset 
 