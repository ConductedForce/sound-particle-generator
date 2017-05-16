'''
liveFile.py
Obtains a File and returns frameData. 
'''

import pyaudio
import wave
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMainWindow

class file():
    CHUNK = 2048
    p = pyaudio.PyAudio()

    def __init__(self, **kwargs):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(QMainWindow(),"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        #if fileName:
            #filename = "input/The Normandy Reborn.wav"
        self.wf = wave.open(fileName, 'rb') #reads the file, sets to read only
        #print("File Read")
        self.swidth = self.wf.getsampwidth()
        self.RATE = self.wf.getframerate()

        
        self.stream = self.p.open(format =
                        self.p.get_format_from_width(self.swidth),
                        channels = self.wf.getnchannels(),
                        rate = self.RATE,
                        output = True)

    #while len(data) > 0:
    def getFileChunkData(self):
        data = self.wf.readframes(self.CHUNK) #reads file data
        self.stream.write(data) #plays audio
        return ((data, self.CHUNK, self.swidth ), self.RATE) #returns chunk

    def killFile(self):
        self.stream.close()
        self.p.terminate()
