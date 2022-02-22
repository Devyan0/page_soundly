"""
sample_short.wav
Duration-0:05 minutes
Codec: PCM S16 LE (s16l)
Channels: Stereo
Sample rate: 44100 Hz
Bits per sample: 16

sample.wav
Duration-0:13 minutes
Codec: PCM S16 LE (s16l)
Channels: Stereo
Sample rate: 44100 Hz
Bits per sample: 16

"""

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print('test sounds running ...')

    # audio_path = 'sample_short.wav'
    audio_path = 'sample.wav'
    # audio_path = librosa.example('nutcracker')

    # load wave form and store sampling rate
    y, sr = librosa.load(audio_path)

    # run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print(f'estimated tempo: {tempo} beats / min')

    # convert the frame indices of beat events into timestamps
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    # plot amplitude in time domain
    plt.figure(figsize=(14, 5))
    # librosa.display.waveshow(y, sr=sr)
    # plt.show()

    # transform to frequency domain using stft(Short Time Fourier Transform)
    Y = librosa.stft(y)
    Ydb = librosa.amplitude_to_db(abs(Y))
    librosa.display.specshow(Ydb, sr=sr, x_axis='time', y_axis='hz')
    plt.show()

