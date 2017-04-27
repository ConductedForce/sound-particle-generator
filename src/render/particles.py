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

        def move(self, points):
            for p in points:
                dis = math.sqrt(math.pow(self.x-p.x,2) + math.pow(self.y-p.y,2))
                #if dis > 520:
                # if self.x and self.y are (x) distance from p.x and p.y
                # do a thing
                #self.x -= random.randint(1,300)
                #if self.x <100:
                #   self.x+=random.randint(1,80)
                #self.y += random.randint(1,100)
                #distanst to the point 
                if dis > 20:
                     #What you want the pixels to do once they reach/past this distanst
                     #moves to the left 
                    self.x = random.randint(-1,900)
                #if self.x >= 100:
                    #self.x +=random.randint(50,700)
                # if self.x >= 625:
                 #self.x += random.randint(50,700)
                    #they go down
                    self.y =random.randint(1,800)
                # if self.y >=150:
                #self.y +=random.randint(50,900)

        def move2(self):
            if self.y == 0:
                self.y = random.randint(0, 100)
            else:
                self.y += 3
            self.x -= random.randint(0, 100)
        def move3(self):
            if self.y == 500:
                self.y = random.randint(0,100)
            else:
                self.y += 1
            self.x -= random.randint(0,10)

class Point():
        def __init__(self, startx, starty):
            self.x = startx
            self.y = starty

class Render():
    def __init__(self):
        infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
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
            self.particles.append( Particle(0, 500, col) )

    def draw(self, points):
        self.screen.fill(self.black)
        for p in self.particles:
            p.move(points)
            pygame.draw.circle(self.screen, p.col, (p.x, p.y), 2)
        

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
    for d in range(5):
        points.append( Point(random.randint(-1,100), random.randint(-1,100)) )

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
