import numpy as np
import matplotlib.pyplot as plt
import librosa

y, sr = librosa.load(librosa.ex('trumpet'))
S = np.abs(librosa.stft(y))

fig,ax=plt.subplots()
img = librosa.display.specshow(librosa.amplitude_to_db(S,ref=np.max),y_axis='log',x_axis='time',ax=ax)
ax.set_title('Power Spectrogram')
fig.colorbar(img,ax=ax,format="%+2.0f dB")
plt.show()
