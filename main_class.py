
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from Constellation_map import *
from Comparison import is_same_sound_db
from ListeMusique import *

listeMusiques=ListeMusiques()

# record files

filename1 = "songs/bakermat.mp3"
filename2 = "songs/Eminem.mp3"
filename3 = "songs/Mome.mp3"
filename4 = "songs/record1.mp3"
filenames=[filename1,filename2,filename3,filename4]

spectrogram_filename=Spectrogram()
spectrogram_filename.compute_spectrogram(filename1)
spectrogram=spectrogram_filename.get_spectrogram()

constellation_filename1=Constellation()
constellation_filename1.constellation_map(spectrogram)
constellation=constellation_filename1.get_cmap()

listeMusiques.ajouter_musique('bakermat','bakermat',constellation_filename1)
listeMusiques.afficher_infos()
