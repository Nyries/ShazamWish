from Constellation_map import constellation_map,compute_spectrogram,plot_constellation_map
import numpy as np
import matplotlib.pyplot as plt 
from scipy import ndimage

filename1="songs/Eminem.mp3"
filename2="songs/Mome.mp3"

def match_binary_matrices_tol(C_ref, C_est, tol_freq=5, tol_time=0):
    """| Compare binary matrices with tolerance
    | Note: The tolerance parameters should be smaller than the minimum distance of
      peaks (1-entries in C_ref ad C_est) to obtain meaningful TP, FN, FP values

    Notebook: C7/C7S1_AudioIdentification.ipynb

    Args:
        C_ref (np.ndarray): Binary matrix used as reference
        C_est (np.ndarray): Binary matrix used as estimation
        tol_freq (int): Tolerance in frequency direction (vertical) (Default value = 0)
        tol_time (int): Tolerance in time direction (horizontal) (Default value = 0)

    Returns:
        TP (int): True positives
        FN (int): False negatives
        FP (int): False positives
        C_AND (np.ndarray): Boolean mask of AND of C_ref and C_est (with tolerance)
    """
    assert C_ref.shape == C_est.shape, "Dimensions need to agree"
    N = np.sum(C_ref)
    M = np.sum(C_est)
    # Expand C_est with 2D-max-filter using the tolerance parameters
    C_est_max = ndimage.maximum_filter(C_est, size=(2*tol_freq+1, 2*tol_time+1),
                                       mode='constant')
    C_AND = np.logical_and(C_est_max, C_ref)
    TP = np.sum(C_AND)
    FN = N - TP
    FP = M - TP
    return TP, FN, FP, C_AND

def compare_constellation_maps(fn_wav_D, fn_wav_Q, dist_freq = 11, dist_time = 5, tol_freq = 5, tol_time = 1):
    Y_D = compute_spectrogram(fn_wav_D)
    Cmap_D = constellation_map(Y_D, dist_freq, dist_time)
    Y_Q = compute_spectrogram(fn_wav_Q)
    Cmap_Q = constellation_map(Y_Q, dist_freq, dist_time)

    TP, FN, FP, Cmap_AND = match_binary_matrices_tol(Cmap_D, Cmap_Q, 
                                                     tol_freq=tol_freq, tol_time=tol_time)
    title=r'Matching result (tol_freq=%d and tol_time=%d): TP=%d, FN=%d, FP=%d' % \
        (tol_freq,tol_time, TP, FN, FP)
    fig, ax, im = plot_constellation_map(Cmap_AND, color='green', s=200, marker='+', title=title)
    n, k = np.argwhere(Cmap_D == 1).T
    ax.scatter(k, n, color='r', s=50, marker='o')
    n, k = np.argwhere(Cmap_Q == 1).T
    ax.scatter(k, n, color='cyan', s=20, marker='o')
    plt.legend(['Matches (TP)', 'Reference', 'Estimation'], loc='upper right', framealpha=1)
    plt.tight_layout()
    plt.show()

def is_same_sound(filename1,filename2,dist_freq=15, dist_time=15,thresh=0.7,tol_freq=5, tol_time=5):
    Y_D = compute_spectrogram(filename1)
    Cmap_D = constellation_map(Y_D, dist_freq, dist_time)
    Y_Q = compute_spectrogram(filename2)
    Cmap_Q = constellation_map(Y_Q, dist_freq, dist_time)

    TP, FN, FP, Cmap_AND = match_binary_matrices_tol(Cmap_D, Cmap_Q, tol_freq=tol_freq, tol_time=tol_time)
    True_ref=np.sum(Cmap_D)
    True_AND=np.sum(Cmap_AND)
    if True_AND/True_ref>thresh:
        return True
    else:
        return False

def is_same_sound_db(Cmap_record,Cmap_ref,dist_freq=15, dist_time=15,thresh=0.7,tol_freq=5, tol_time=5):

    TP, FN, FP, Cmap_AND = match_binary_matrices_tol(Cmap_record, Cmap_ref, tol_freq=tol_freq, tol_time=tol_time)
    True_ref=np.sum(Cmap_ref)
    True_AND=np.sum(Cmap_AND)
    if True_AND/True_ref>thresh:
        return True
    else:
        return False
#is_same_sound(filename1,filename1)
