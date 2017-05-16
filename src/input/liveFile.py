import pyaudio
import wave
import numpy as np
from PyQt5.QtWidgets import QFileDialog

class file():
    CHUNK = 1024
    p = pyaudio.PyAudio()

    def __init__(self, **kwargs):
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        #if fileName:
        filename = "input/The Normandy Reborn.wav"
        self.wf = wave.open(filename, 'rb') #reads the file, sets to read only
        #print("File Read")
        swidth = self.wf.getsampwidth()
        RATE = 44100

        
        self.stream = self.p.open(format =
                        self.p.get_format_from_width(self.wf.getsampwidth()),
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

import os

def downsampleWav(src, dst, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
    if not os.path.exists(src):
        print ('Source not found!')
        return False

    print (dst);
    #if not os.path.exists(os.path.dirname(dst)):
        #os.makedirs(os.path.dirname(dst))

    try:
        s_read = wave.open(src, 'r')
        s_write = wave.open(dst, 'w')
    except:
        print ('Failed to open files!')
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
    except:
        print ('Failed to downsample wav')
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except:
        print ('Failed to write wav')
        return False
 
    try:
        s_read.close()
        s_write.close()
    except:
        print ('Failed to close wav files')
        return False

    return True

'''os.getcwd() + "\\" + '''
result = downsampleWav("input\The Normandy Reborn.wav", "input\test.wav") 
print(result);