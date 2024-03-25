import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

filename = "songs/Mome.mp3"

def constellation_map(Y,dist_freq=7,dist_time=7,thresh=0.01):
    """Y: array numpy 2D with the data of chromagram"""

    result = ndimage.maximum_filter(Y, size=[2*dist_freq+1, 2*dist_time+1], mode='constant')
    Cmap = np.logical_and(Y == result, result > thresh)
    return Cmap


def plot_constellation_map(Cmap, Y=None, xlim=None, ylim=None, title='',xlabel='Time (sample)', ylabel='Frequency (bins)',s=5, color='r', marker='o', figsize=(7, 3), dpi=72):

    if Cmap.ndim>1:
        M,N=Cmap.shape
    else:
        M=Cmap.shape[0]
        N=1
    
    if Y is None:
        Y=np.zeros((M,N))

    fig, ax = plt.subplots(1, 1, figsize=(7, 3), dpi=dpi)
    im = ax.imshow(Y, origin='lower', aspect='auto', cmap='gray_r', interpolation='nearest')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    Fs = 1
    if xlim is None:
        xlim = [-0.5/Fs, (N-0.5)/Fs]
    if ylim is None:
        ylim = [-0.5/Fs, (M-0.5)/Fs]
    #ax.set_xlim(xlim)
    #ax.set_ylim(ylim)
    n, k = np.argwhere(Cmap == 1).T
    ax.scatter(k, n, color=color, s=s, marker=marker)
    plt.tight_layout()

    return fig, ax, im

def compute_spectrogram(audio_file,N=2048,H=1024,Fs=22050,bin_max=128,frame_max=5000):
    y,fs=librosa.load(audio_file)
    y_duration=len(y)/Fs
    Y=librosa.stft(y, window='hann')
    print('a')
    if bin_max is None:
        bin_max = Y.shape[0]
    if frame_max is None:
        frame_max = Y.shape[0]
    Y = np.abs(Y[:bin_max, :frame_max])

    return Y

Y=compute_spectrogram(filename)
Cmap_naive=constellation_map(Y)

fig,ax,im=plot_constellation_map(Cmap_naive,Y)
print(Cmap_naive.shape)
plt.show()