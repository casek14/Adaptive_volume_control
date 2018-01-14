''' test of the audio record '''

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAWE_OUTPUT_FILENAME = 'output.wav'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAWE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
