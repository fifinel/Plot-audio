import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def plot_waveform(file_path):
    # Read the audio file
    sample_rate, data = wavfile.read(file_path)

    # Check if the audio is stereo or mono
    if len(data.shape) == 2:
        data = data[:, 0]  # Use only the first channel for stereo audio

    # Create time array for plotting
    duration = len(data) / sample_rate
    time = np.linspace(0., duration, len(data))

    # Plot the waveform
    plt.figure(figsize=(12, 6))
    plt.plot(time, data, label="Audio Signal")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Audio Signal Waveform")
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
audio_file_path = r"C:\Users\User\Downloads\sound.wav"
plot_waveform(audio_file_path)
