# wave data   -xlxw

# import
import wave as we
import numpy as np
import matplotlib.pyplot as plt


# nchannels:声道数
# sampwidth:量化位数（byte）
# framerate:采样频率
# nframes:采样点数
wavpath = "E:\\1.wav"


def wavread(path):
    wavfile = we.open(path, "rb")
    params = wavfile.getparams()
    wavchl, sampwidth, framerate, nframes = params[:4]
    datawav = wavfile.readframes(nframes)
    wavfile.close()
    wavdata = np.fromstring(datawav, dtype=np.short)
    wavdata.shape = -1, wavchl
    wavdata = wavdata.T
    wavtime = np.arange(0, nframes) * (1.0 / framerate)
    return wavchl, wavdata, wavtime


def main():
    path = wavpath
    wavchl, wavdata, wavtime = wavread(path)
    plt.title("Night.wav's Frames")
    colors = np.array(["red", "green"])
    for i in range(wavchl):
        plt.subplot(np.add(i, 211))
        plt.plot(wavtime, wavdata[i], colors[i])

    plt.show()


main()
