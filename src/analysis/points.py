import pyaudio
import wave
import numpy as np

class Point():
        def __init__(self, startx, starty):
            self.x = startx
            self.y = starty

def analyze(data, RATE):
    frameData, swidth, chunk = data
    window = np.blackman(chunk)
    # unpack the data and times by the hamming window
    #bite = bytes(8)
    fmt = "%dh"%(len(frameData)/2)
    #fmt = "%dh"
    daData = len(frameData)
    print (daData)
    print (wave.struct.calcsize(fmt))
    #print(wave.struct.calcsize(bite))
    #if daData == 0 and wave.struct.calcsize(fmt) != 0:
        #fmt = 0
    aValue = wave.struct.unpack(fmt, frameData)
    indata = np.array(aValue)#*window
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
        print ("The freq is %f kHz." % (thefreq/1000))
    else:
        thefreq = which*RATE/chunk
        print( "The freq is %f kHz." % (thefreq/1000))



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