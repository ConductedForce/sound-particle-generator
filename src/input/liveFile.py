import pyaudio
import wave
import numpy as np
from PyQt5.QtWidgets import QFileDialog

class file():
    CHUNK = 2048
    p = pyaudio.PyAudio()

    def __init__(self, **kwargs):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.wf = wave.open(filename, 'rb') #reads the file, sets to read only
        #print("File Read")
        swidth = self.wf.getsampwidth()
        RATE = self.wf.getframerate()

        
        self.stream = self.p.open(format =
                        p.get_format_from_width(self.wf.getsampwidth()),
                        channels = self.wf.getnchannels(),
                        rate = RATE,
                        output = True)

    #while len(data) > 0:
    def getFileChunkData(self):
        data = self.wf.readframes(self.CHUNK) #reads file data
        self.stream.write(data) #plays audio
        return data #returns chunk

    def killFile(self):
        self.stream.close()
        self.p.terminate()

