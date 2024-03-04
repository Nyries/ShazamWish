import librosa
import numpy as np
import matplotlib.pyplot as plt

filename = "music.mp3"


y, sr = librosa.load(filename, sr = None,  offset=15.0, duration=5.0)




def fingerprint(audio_file):
    # Load the audio file with librosa
    y, sr  = librosa.load(audio_file, sr=None)

    print ('Floating point time series of the audio files : \n', y)

    print('Sampling frequency : \n',sr)

    print(librosa.get_duration(y=y, sr=sr))


    # Determinate the audio file spectrogram
    spectrogram = np.abs(librosa.stft(y))

    print('Spectrogram values : \n',spectrogram)


    # Convert into a chromagram
    chromagram = librosa.feature.chroma_stft(S=spectrogram, sr=sr)

    print('Chromagram Values : \n',chromagram)


    # Convert in a fingerprint
    fingerprint = np.argmax(chromagram, axis=0)

    
    print('Fingerprint : \n',fingerprint.tolist())
    #Plotting spectrogram and chromagram
    fig, ax = plt.subplots(nrows=3, sharex=True)
    img = librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max),y_axis='log', x_axis='time', ax=ax[0])
    fig.colorbar(img, ax=[ax[0]])
    ax[0].label_outer()

    img = librosa.display.specshow(chromagram, y_axis='chroma', x_axis='time', ax=ax[1])
    fig.colorbar(img, ax=[ax[1]])

    plt.show()

    return fingerprint.tolist()


fingerprint(filename)
