''' Make wire between input and output '''
import pyaudio
import numpy as np
CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("*** RECORDING")
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    stream.write(data, CHUNK)
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print data

print("*** DONE RECORDING")

stream.stop_stream()
stream.close()

p.terminate()
