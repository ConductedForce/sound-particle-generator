import pyaudio
import wave
import numpy as np


class file():

    def readFile():
        CHUNK = 2048

        filename = "output.wav"
        wf = wave.open(filename, 'rb') #reads the file, sets to read only
        #print("File Read")
        swidth = wf.getsampwidth()
        RATE = wf.getframerate()

        p = pyaudio.PyAudio()
        stream = p.open(format =
                        p.get_format_from_width(wf.getsampwidth()),
                        channels = wf.getnchannels(),
                        rate = RATE,
                        output = True)

    #while len(data) > 0:
    def getFileChunkData():
        data = wf.readframes(CHUNK) #reads file data
        stream.write(data) #plays audio
        return data #returns chunk

    def killFile():
        stream.close()
        p.terminate()

