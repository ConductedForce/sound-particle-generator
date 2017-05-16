import random 
from pygame.locals import *
import math
import render.pathMap as pt
import pygame

class Particle():
        #im in the particle
        pathPoint =  0
        onPath = False
        speed = 1

        def __init__(self, startx, starty, col):
            self.x = startx
            self.y = random.randint(0, starty)
            self.col = col
            self.sx = startx
            self.sy = starty
        
        def pdis(self,points):
            store=[]
            for p in points:
                dis = math.sqrt(math.pow(self.x-p.x,2) + math.pow(self.y-p.y,2))
                store.append(dis)
                low = min(float(s) for s in store)
            return low

        def move(self, points, iO,path):
                dis = self.pdis(points)
                #point loction in here / behavior
                
                #firstly, we want to get particles to path
                #then we must get them moving
                #as they are moving, they must have random value x radius from path point
                #generate new position with cos/sin
                if self.onPath is True:
                    if self.pathPoint >= len(path)-1:
                        self.pathPoint = 0
                    self.x = path[self.pathPoint+1].x
                    self.y = path[self.pathPoint+1].y
                else:
                    self.x = random.randint(0, iO.current_w)
                    self.y = random.randint(0, iO.current_h)
                    if dis < 50:
                        self.onPath = True
                        self.pathPoint = random.randint(0,len(path)-1)
                        self.x = path[self.pathPoint].x
                        self.y = path[self.pathPoint].y
                        

                #circle calculation
                #t = 2*pi*random
                #r = random[0,20]
                #Point( cos(), sin)

                #speed value will determine loop speed
                self.pathPoint += 1
                                
class Point():
        def __init__(self, startx, starty):
            self.x = startx
            self.y = starty

class Render():

    def __init__(self):
        self.infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.infoObject.current_w, self.infoObject.current_h))
        pygame.init()

        self.black = (0,0,0)
        self.grey = (145,145,145)
        self.light_grey = (192,192,192)
        self.dark_grey = (183, 183, 183)
        self.blue = (0,153,153)
        self.red = (225,0,0)
        self.green =(103,255,255)
        self.agreen = (124,252,0)
        self.light_blue=(0,255,255)

        self.particles = [] #particles

        self.x1=0
        self.y3=500

    def make(self):
        for part in range(1000):
            if part % 2 > 0: col = self.green
           #elif part % 5 > 0: col = dark_grey
            elif part % 3 > 0: col = self.light_blue
            else: col = self.blue
            self.particles.append( Particle(0, 1000, col) )
                
    def readPath(self, mpoints):
            path = pt.Path().findpath(mpoints)
            return path
            #loop through path
            #determine type of i
            #i.type equals road.Line().type
            #extend pathway[] (i)
            # no else
            #for pot in path:
             #   pygame.draw.circle(self.screen, self.agreen, (pot.x, pot.y), 10)

            
            #road = None
            #path = None
            
   
    def draw(self, points,path,feq):
         self.screen.fill(self.black)
         if feq <= 500:
           acolor = self.blue
         if feq >= 500 and feq <= 900:
           acolor = self.agreen 
         if feq > 900 :
           acolor = self.red
         for p in self.particles:
            p.move(points, self.infoObject, path)
            pygame.draw.circle(self.screen, acolor, (p.x, p.y), 2)
         for po in points:
            pygame.draw.circle(self.screen, self.red, (po.x, po.y), 10)
       #for pot in pathway:
           #pygame.draw.circle(self.screen, self.agreen, (pot.x, pot.y), 7)