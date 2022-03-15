"""
Notebook for streaming data from a microphone in realtime

audio is captured using pyaudio
then converted from binary data to ints using struct
then displayed using matplotlib

scipy.fft pack computes the FFT
"""
import sys
import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import time
from tkinter import TclError
from scipy.signal import find_peaks

# constants
CHUNK = 1024 * 2             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second

# create matplotlib figure and axes
fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))

# pyaudio class instance
p = pyaudio.PyAudio()

# stream object to get data from microphone
stream = p.open(
    format=FORMAT,           #set the depth of bits, FORMAT = pyaudio.paInt16 (bit depth is 16 bits)
    channels=CHANNELS,
    rate=RATE,               #Sampling rate
    input=True,              #For opening input stream
    output=True,
    frames_per_buffer=CHUNK  #Size of chunck (Chunk = Sample per frame)
)

# variable for plotting
x = np.arange(0, 2 * CHUNK, 2)       # samples (waveform)
xf = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)

# create a line object with random data
line, = ax1.plot(x, np.zeros(CHUNK), '-', lw=2)



# create semilogx line for spectrum
line_fft, = ax2.plot(xf, np.zeros(CHUNK), '-', lw=2)

# format waveform axes
ax1.set_title('AUDIO WAVEFORM')
ax1.set_xlabel('samples')
ax1.set_ylabel('volume')
ax1.set_ylim(0, 255)
ax1.set_xlim(0, 2 * CHUNK)
plt.setp(ax1, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

# format spectrum axes
ax2.set_xlim(0, 22528)
ax2.set_ylim(0, 10000)


plt.show(block=False) #creates an empty frozen window

print('stream started')

# for measuring frame rate
frame_count = 0
start_time = time.time()

while True:

    # binary data
    data = stream.read(CHUNK)

    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = np.array(data_int, dtype='b')[::2] + 128

    line.set_ydata(data_np)

    # compute FFT and update line
    yf = fft(data_int)
    freq_value = np.abs(yf[0:CHUNK]) * 2 / (256 * CHUNK)
    line_fft.set_ydata(10000*freq_value)

    # print("데이터 들어오는 것", data_int)
    # print("fft 데이터", yf)

    np.set_printoptions(threshold=sys.maxsize)
    freq_value[0]=0
    #print("Expected_Frequency",10000*freq_value)
    max_value_frequency = 22 * np.argmax(freq_value)
    #print(max_value_frequency)

    if max_value_frequency>213.7 and max_value_frequency<226.4:
        print(f'음: 3 옥타브 라')
    elif max_value_frequency>226.4 and max_value_frequency<239.9:
        print(f'음: 3 옥타브 라#')
    elif max_value_frequency > 239.9 and max_value_frequency < 254.18:
        print(f'음: 3 옥타브 시')
    elif max_value_frequency > 254.18 and max_value_frequency < 269.3:
        print(f'음: 4 옥타브 도')
    elif max_value_frequency>269.3 and max_value_frequency<285.3:
        print(f'음: 4 옥타브 도#')
    elif max_value_frequency>285.3 and max_value_frequency<302.3:
        print(f'음: 4 옥타브 레')
    elif max_value_frequency>302.3 and max_value_frequency<320.24:
        print(f'음: 4 옥타브 레#')
    elif max_value_frequency > 320.24 and max_value_frequency < 339.3:
        print(f'음: 4 옥타브 미')
    elif max_value_frequency > 339.3 and max_value_frequency < 359.46:
        print(f'음: 4 옥타브 파')
    elif max_value_frequency > 359.46 and max_value_frequency < 380.84:
        print(f'음: 4 옥타브 파#')
    elif max_value_frequency > 380.84 and max_value_frequency < 403.48:
        print(f'음: 4 옥타브 솔')
    elif max_value_frequency > 403.48 and max_value_frequency < 427.47:
        print(f'음: 4 옥타브 솔#')
    elif max_value_frequency > 427.47 and max_value_frequency < 452.89:
        print(f'음: 4 옥타브 라')
    elif max_value_frequency > 452.89 and max_value_frequency < 479.82:
        print(f'음: 4 옥타브 라#')
    elif max_value_frequency > 479.82 and max_value_frequency < 508.36:
        print(f'음: 4 옥타브 시')
    elif max_value_frequency > 508.36 and max_value_frequency < 538.58:
        print(f'음: 5 옥타브 도')
    elif max_value_frequency > 538.58 and max_value_frequency < 570.61:
        print(f'음: 5 옥타브 도#')
    elif max_value_frequency > 570.61 and max_value_frequency < 604.54:
        print(f'음: 5 옥타브 레')
    elif max_value_frequency > 604.54 and max_value_frequency < 640.49:
        print(f'음: 5 옥타브 레#')
    elif max_value_frequency > 640.49 and max_value_frequency < 678.57:
        print(f'음: 5 옥타브 미')
    elif max_value_frequency > 678.57 and max_value_frequency < 718.92:
        print(f'음: 5 옥타브 파')
    elif max_value_frequency > 718.92 and max_value_frequency < 761.67:
        print(f'음: 5 옥타브 파#')
    elif max_value_frequency > 761.67 and max_value_frequency < 806.96:
        print(f'음: 5 옥타브 솔')
    elif max_value_frequency > 806.96 and max_value_frequency < 854.95:
        print(f'음: 5 옥타브 솔#')
    elif max_value_frequency > 854.95 and max_value_frequency < 905.79:
        print(f'음: 5 옥타브 라')
    elif max_value_frequency > 905.79 and max_value_frequency < 959.65:
        print(f'음: 5 옥타브 라#')
    elif max_value_frequency > 959.65 and max_value_frequency < 1016.71:
        print(f'음: 5 옥타브 시')
    elif max_value_frequency > 1016.71 and max_value_frequency < 1077.17:
        print(f'음: 6 옥타브 도')
    elif max_value_frequency > 1077.17 and max_value_frequency < 1141.22:
        print(f'음: 6 옥타브 도#')
    elif max_value_frequency > 1141.22 and max_value_frequency < 1209.1:
        print(f'음: 6 옥타브 레')
    elif max_value_frequency > 1209.1 and max_value_frequency < 1280.97:
        print(f'음: 6 옥타브 레#')
    elif max_value_frequency > 1280.97 and max_value_frequency < 1357.15:
        print(f'음: 6 옥타브 미')
    elif max_value_frequency > 1357.15 and max_value_frequency < 1437.85:
        print(f'음: 6 옥타브 파')
    elif max_value_frequency > 1437.85 and max_value_frequency < 1523.34:
        print(f'음: 6 옥타브 파#')
    elif max_value_frequency > 1523.34 and max_value_frequency < 1613.93:
        print(f'음: 6 옥타브 솔')
    elif max_value_frequency > 1613.93 and max_value_frequency < 1709.9:
        print(f'음: 6 옥타브 솔#')
    elif max_value_frequency > 1709.9 and max_value_frequency < 1811.57:
        print(f'음: 6 옥타브 라')
    elif max_value_frequency > 1811.57 and max_value_frequency < 1919.29:
        print(f'음: 6 옥타브 라#')
    elif max_value_frequency > 1919.29 and max_value_frequency < 2033.42:
        print(f'음: 6 옥타브 시')
    elif max_value_frequency > 2033.42 and max_value_frequency < 2154.33:
        print(f'음: 7 옥타브 도')
    elif max_value_frequency > 2154.33 and max_value_frequency < 2282.44:
        print(f'음: 7 옥타브 도#')
    elif max_value_frequency > 2282.44 and max_value_frequency < 2418.16:
        print(f'음: 7 옥타브 레')
    elif max_value_frequency > 2418.16 and max_value_frequency < 2561.95:
        print(f'음: 7 옥타브 레#')
    elif max_value_frequency > 2561.95 and max_value_frequency < 2714.29:
        print(f'음: 7 옥타브 미')
    elif max_value_frequency > 2714.29 and max_value_frequency < 2875.69:
        print(f'음: 7 옥타브 파')
    elif max_value_frequency > 2875.69 and max_value_frequency < 3046.69:
        print(f'음: 7 옥타브 파#')
    elif max_value_frequency > 3046.69 and max_value_frequency < 3227.85:
        print(f'음: 7 옥타브 솔')
    elif max_value_frequency > 3227.85 and max_value_frequency < 3419.79:
        print(f'음: 7 옥타브 솔#')
    elif max_value_frequency > 3419.79 and max_value_frequency < 3623.14:
        print(f'음: 7 옥타브 라')
    elif max_value_frequency > 3623.14 and max_value_frequency < 3838.59:
        print(f'음: 7 옥타브 라#')

    #max_index = np.argmax(freq_value)
    #print(max_index)

    #peaks, _ = find_peaks(freq_value, height=0.3)
    #print(peaks)



    # update figure canvas
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1

    except TclError:

        # calculate average frame rate
        frame_rate = frame_count / (time.time() - start_time)

        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break