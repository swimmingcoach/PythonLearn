# wave data   -xlxw

# import
import wave as we
import numpy as np
import matplotlib.pyplot as plt


# nchannels:声道数
# sampwidth:量化位数（byte）
# framerate:采样频率
# nframes:采样点数

def wavread(path):
    wavfile = we.open(path, "rb")
    params = wavfile.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    datawav = wavfile.readframes(nframes)
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short)
    datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, nframes) * (1.0 / framerate)
    return nchannels, datause, time


def main():
    path = input("The Path is:")
    wavchl, wavdata, wavtime = wavread(path)
    plt.title("Night.wav's Frames")
    for i in range(wavchl):
        plt.subplot(np.add(i, 211))
        plt.plot(wavtime, wavdata[i])

    plt.show()


main()
