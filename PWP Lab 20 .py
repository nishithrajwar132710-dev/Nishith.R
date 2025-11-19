import soundfile as sf
# Load audio file
audio, sample_rate = sf.read(r'C:/Users/devah/Downloads/Nani - Sound Effect.mp3')
sf.write('Deva_AudioProcessing_1.wav', audio, 22050)

audio, sample_rate = sf.read(r'C:/Users/devah/Downloads/Nani - Sound Effect.mp3')
sf.write('Deva_AudioProcessing_2.wav', audio, 88200)

import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
# Load audio file
#audio, sample_rate = sf.read('audio_file.wav')
# Create time axis
time = np.arange(0, len(audio)) / 44100
# Plot audio signal
plt.plot(time, audio)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file(r'C:/Users/devah/Downloads/Nani - Sound Effect.mp3')

# Add fade in effect
audio_fade_in = audio.fade_in(2000)  # 2 seconds

# Export audio file with fade in effect
audio_fade_in.export('audio_file_fade_in.wav', format='wav')
