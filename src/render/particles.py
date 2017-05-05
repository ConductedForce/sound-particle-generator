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
            for count, p in enumerate(points):
                dis = math.sqrt(math.pow(self.x-p.x,2) + math.pow(self.y-p.y,2))
                store.append(dis)
                low = min(float(s) for s in store)
            return (low, count)

        def move(self, points, iO, pathway):
                dis, count = self.pdis(points)
                #point loction in here / behavior
               
                #firstly, we want to get particles to path
                #then we must get them moving
                #as they are moving, they must have random value x radius from path point
                #generate new position with cos/sin
                if onPath is True:
                    if pathPoint is pathway.size:
                        pathPoint = 0
                    self.x = pathway[pathPoint+1].x
                    self.y = pathway[pathPoint+1].y

                else:
                    self.x = random.randint(0, iO.current_w)
                    self.y = random.randint(0, iO.current_h)
                    if dis < 20:
                        onPath = True
                        self.x = pathway[pathPoint].x
                        self.y = pathway[pathPoint].y
                        

                #circle calculation
                #t = 2*pi*random
                #r = random[0,20]
                #Point( cos(), sin)

                #speed value will determine loop speed
                pathPoint += 1
                                
class Point():
        def __init__(self, startx, starty):
            self.x = startx
            self.y = starty

class Render():
    pathway = []

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
            road = pt.Path(mpoints)
            path = road.path1
            #loop through path
            #determine type of i
            #i.type equals road.Line().type
            #extend pathway[] (i)
            # no else
            for i in path:
                if type(i) == type(road.Line()):
                    self.pathway.extend(i.line)
                if type(i) == type(road.SemiCircle()):
                    self.pathway.extend(i.circle)
            
    def draw(self, points):
        self.screen.fill(self.black)
        for p in self.particles:
            p.move(points, self.infoObject, self.pathway)
            pygame.draw.circle(self.screen, p.col, (p.x, p.y), 2)
        for po in points:
            pygame.draw.circle(self.screen, self.red, (po.x, po.y), 10)

def main():
    pygame.init()
    
    black = (0,0,0)
    grey = (145,145,145)
    light_grey = (192,192,192)
    dark_grey = (183, 183, 183)
    blue = (0,153,153)
    red = (225,0,0)
    green =(103,255,255)
    light_blue=(0,255,255)

    clock = pygame.time.Clock()

    points = []
    for d in range(10):
        points.append( Point(random.randint(-1,800), random.randint(-1,700)) )

    activeRender = Render()
    activeRender.make()
   
    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        
        activeRender.draw(points)

        pygame.display.flip()
        clock.tick(80)
    pygame.quit()

if __name__ == "__main__":
    main()
