import pygame,random 
from pygame.locals import *
import math

xmax = 1000    #width of window
ymax = 1000     #height of window

x1=0
x3=500
x2=999
y1=0
y3=500
y2=999

class Smoke():
    

    def __init__(self, startx, starty, col):
        self.x = startx
        self.y = random.randint(0, starty)
        self.col = col
        self.sx = startx
        self.sy = starty

    def move(self, points):
        for p in points:
            dis = math.sqrt(math.pow(self.x-p.x,2) + math.pow(self.y-p.y,2))
            if dis <= 20:
             # if self.x and self.y are (x) distance from p.x and p.y
             # do a thing
              self.x -= 3
              self.y -= 6
            if dis >= 20:
              self.x += 3
              self.y += 6
                   
    def move2(self):
        if self.y == 0:
           self.y = random.randint(0, 600)
        else:
            self.y += 3
        self.x -= random.randint(0, 10)
    def move3(self):
        if self.y == 500:
            self.y = random.randint(0,500)
        else:
            self.y += 1
        self.x -= random.randint(0,10)

class poops():
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty



def draw(points):
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    black = (0,0,0)
    grey = (145,145,145)
    light_grey = (192,192,192)
    dark_grey = (183, 183, 183)
    blue = (0,153,153)
    red = (225,0,0)
    green =(103,255,255)
    light_blue=(0,255,255)

    particles = []
    for part in range(1000):
        if part % 2 > 0: col = green
        #elif part % 5 > 0: col = dark_grey
        elif part % 3 > 0: col = light_blue
        else: col = blue
        particles.append( Smoke(x1, y3, col) )

    for p in particles:
            p.move(points)
            pygame.draw.circle(screen, p.col, (p.x, p.y), 2)



 
def main():
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    black = (0,0,0)
    grey = (145,145,145)
    light_grey = (192,192,192)
    dark_grey = (183, 183, 183)
    blue = (0,153,153)
    red = (225,0,0)
    green =(103,255,255)
    light_blue=(0,255,255)

    clock = pygame.time.Clock()


    particles = []
    for part in range(1000):
        if part % 2 > 0: col = green
        #elif part % 5 > 0: col = dark_grey
        elif part % 3 > 0: col = light_blue
        else: col = blue
        particles.append( Smoke(x1, y3, col) )

    particles1 = []
    for part in range(1000):
        if part % 2 > 0: col = green
        #elif part % 5 > 0: col = dark_grey
        elif part % 3 > 0: col = light_blue
        else: col = blue
        particles1.append( Smoke(x3, y1, col) )
    
    particles2 = []
    for part in range(1000):
        if part % 2 > 0: col = green
        #elif part % 5 > 0: col = dark_grey
        elif part % 3 > 0: col = light_blue
        else: col = blue
        particles2.append( Smoke(x2, y3, col) )
    
    particles3 = []
    for part in range(1000):
        if part % 2 > 0: col = green
        #elif part % 5 > 0: col = dark_grey
        elif part % 3 > 0: col = light_blue
        else: col = blue
        particles3.append( Smoke(x3, y2, col) )

    points = []
    for d in range(5):
        points.append( poops(random.randint(-1,100), random.randint(-1,100)) )

    
    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(black)
        for p in particles:
            p.move(points)
            pygame.draw.circle(screen, p.col, (p.x, p.y), 2)
        
        #for p in particles1:
           # p.move2()
           # pygame.draw.circle(screen, p.col, (p.x, p.y), 2)

        #for p in particles2:
           # p.move3()
           # pygame.draw.circle(screen, p.col, (p.x, p.y), 2)

        #for p3 in particles3:
            #p3.move()
            #pygame.draw.circle(screen, p3.col, (p3.x, p3.y), 2)
        draw(points)

        pygame.display.flip()
        clock.tick(80)
    pygame.quit()

if __name__ == "__main__":
    main()
