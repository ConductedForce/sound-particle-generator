import pyaudio
import numpy

class mic():
    CHUNK = 1024
    p = pyaudio.PyAudio()

    def __init__(self, **kwargs):
        
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100  
        

        self.stream = self.p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=self.CHUNK)

    def getMicChunkData(self):
          data = self.stream.read(self.CHUNK)
          return data
       

    def killMic(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
