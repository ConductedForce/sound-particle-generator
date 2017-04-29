import pygame,random 
from pygame.locals import *
import math

class Particle():
        def __init__(self, startx, starty, col):
            self.x = startx
            self.y = random.randint(0, starty)
            self.col = col
            self.sx = startx
            self.sy = starty
#im in the partile
        def pdis(self,points):
            store=[]
            for p in points:
                dis = math.sqrt(math.pow(self.x-p.x,2) + math.pow(self.y-p.y,2))
                store.append(dis)
                low = min(float(s) for s in store)
            return low


        def move(self, points, iO):
                p = points[0]
                dis = self.pdis(points)
                 
                #point loction in here / behavior
                #distanst to the point 
                if dis < 20:
                     #What you want the pixels to do once they reach/past this distanst
                     self.x-=9
                     self.x+=19
                     self.y-=9
                     self.y+=19 
                else: 
                    #what the point does if not near the points
                     #moves to the left 
                    self.x = random.randint(-1, iO.current_w)
                                  #they go down
                    self.y =random.randint(1,iO.current_h) 
                    if self.x > iO.current_w:
                        self.x-=60
                    if self.y >iO.current_h:
                        self.y-=60
                    if self.x < 0:
                        self.x +=60
                    if self.y < 0:
                        self.y +=60
        def attract(self,point):
            dx=(self.x-p.x)
            dy=(self.y-p.y)
            dist = math.hypot(dx,dy)
            theta=math.atan2(dy,dx)
            force = 0.2*self.mass*p.mass/dist*2
            self.accelerate((theta-0.5*math.pi,force/self.mass))
            p.accelerate((theta + 0.5* math.pi, force/p.mass))
                                 
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

    def draw(self, points):
        self.screen.fill(self.black)
        for p in self.particles:
            p.move(points, self.infoObject)
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
