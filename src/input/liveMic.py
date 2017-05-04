import pyaudio
import numpy

class mic():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100  
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    def getChunkData():
          data = stream.read(CHUNK)
          return data
       

    def killMic():
        stream.stop_stream()
        stream.close()
        p.terminate()
