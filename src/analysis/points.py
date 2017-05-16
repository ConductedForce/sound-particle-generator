import pyaudio
import wave
import numpy as np

class Point():
        def __init__(self, startx, starty):
            self.x = startx
            self.y = starty

def analyze(frameData):
    # unpack the data and times by the hamming window
    indata = np.array(wave.struct.unpack("%dh"%(len(frameData)/swidth),\
                                         frameData))*window
    # Take the fft and square each value
    fftData=abs(np.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        print ("The freq is %f Hz." % (thefreq))
    else:
        thefreq = which*RATE/chunk
        print( "The freq is %f Hz." % (thefreq))



#append speeds take average

def create(data):
    points = []
    if len(points) != 0:
        points[:] = []    

    points.append(Point( 200, 200 ))
    points.append(Point( 300, 600 ))
    points.append(Point( 1000, 500 ))
    points.append(Point( 750, 150 ))

    return points