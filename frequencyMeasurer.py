import pyaudio
import numpy as np
from scipy.signal import find_peaks

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Start recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")
frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(np.frombuffer(data, dtype=np.int16))

print("Finished recording.")

# Stop recording
stream.stop_stream()
stream.close()
audio.terminate()

# Convert frames to numpy array
audio_data = np.hstack(frames)

# Perform Fourier Transform
fft_spectrum = np.fft.fft(audio_data)
frequencies = np.fft.fftfreq(len(fft_spectrum))

# Take the absolute value of the spectrum and find the peak
fft_spectrum = np.abs(fft_spectrum)
peak_indices, _ = find_peaks(fft_spectrum)
peak_freqs = frequencies[peak_indices]

# Find the frequency with the highest peak
dominant_freq = abs(peak_freqs[np.argmax(fft_spectrum[peak_indices])]) * RATE

print(f"Dominant frequency: {dominant_freq} Hz")
