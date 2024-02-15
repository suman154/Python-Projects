# import required libaries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# sampling frequency
freq = 44100

# recording duration
duration = 10

# start recorder with the given values
# of the duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq
                   , channels=2)


# record audio for the given number of second
sd.wait()


# this will convert the Numpy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)

# convert the Numpy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)