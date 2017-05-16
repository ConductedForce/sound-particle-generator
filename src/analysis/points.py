import pyaudio
import wave
import numpy as np
import pygame

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
        return (thefreq/1000)
    else:
        thefreq = which*RATE/chunk
        print( "The freq is %f kHz." % (thefreq/1000))
        return (thefreq/1000)



#append speeds take average

def create(data):
    points = []
    if len(points) != 0:
        points[:] = []    
    infoObject = pygame.display.Info()
    width = infoObject.current_w
    height = infoObject.current_h
    
    center = Point(width/2, height/2)
    box1 = Point(width/3, height/3)
    box2 = Point(box1.x, box1.y*2)
    box3 = Point(box1.x, height)
    box4 = Point(box1.x*2, box1.y)
    box5 = Point(box1.x*2, box1.y*2)
    box6 = Point(box1.x*2, height)
    box7 = Point(width, box1.y)
    box8 = Point(width, box1.y*2)
    box9 = Point(width, height)

    points.append(Point( (int)(box1.x*.75), (int)(box1.y*.75) ))
    points.append(Point( 300, 600 ))
    points.append(Point( 1000, 500 ))
    points.append(Point( 750, 150 ))
    #points.append(Point( 750, 150 ))
    #points.append(Point( 750, 150 ))
    #points.append(Point( 750, 150 ))
    #points.append(Point( 750, 150 ))



    return points