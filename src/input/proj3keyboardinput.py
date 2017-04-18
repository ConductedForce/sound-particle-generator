'''
Implements mixer to play sound files, sounds can be mapped to keyboard input
Necessary to have sounds files in same file directory
Links to sound libraries:
http://www.findsounds.com/
http://soundcavern.free.fr/guitar/
'''

import pygame,random
from pygame.locals import *

xmax = 1000    #width of window
ymax = 600     #height of window

# VVV Added part VVV
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
try:
    cymbals = pygame.mixer.Sound('cymbals.wav')  #load sound
    bitchin = pygame.mixer.Sound('bitchin.wav')  #load sound
    bassDrum = pygame.mixer.Sound('Bass drum.wav')
    kick = pygame.mixer.Sound('kickatbc.wav')
    hi = pygame.mixer.Sound('hi_tune_4.wav')
except:
    raise UserWarning, "could not load or play soundfiles in 'data' folder :-("


class Smoke():
    def __init__(self, startx, starty, col):
        self.x = startx
        self.y = random.randint(0, starty)
        self.col = col
        self.sx = startx
        self.sy = starty
    def move(self):
        if self.y < 0:
            self.x = self.sx
            self.y = self.sy
        else:
            self.y -= 1
        self.x += random.randint(-1, 2)




def main():
    ##pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    black = (0,0,0)
    grey = (145,145,145)
    light_grey = (192,192,192)
    dark_grey = (183, 183, 183)

    clock = pygame.time.Clock()


    particles = []
    for part in range(600):
        if part % 2 > 0: col = grey
        elif part % 3 > 0: col = dark_grey
        else: col = light_grey
        particles.append( Smoke(0, 600, col) )

    # VVV Added Part VVV
    pressed = pygame.key.get_pressed()
    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True
                elif event.key == pygame.K_z:
                    cymbals.play()
                elif event.key == pygame.K_x:
                    bassDrum.play()
                elif event.key == pygame.K_c:
                    kick.play()
                elif event.key == pygame.K_v:
                    hi.play()
                elif event.key == pygame.K_b:
                    bitchin.play()


        screen.fill(black)
        for p in particles:
            p.move()
            pygame.draw.circle(screen, p.col, (p.x, p.y), 5)

        pygame.display.flip()
        clock.tick(90)
    pygame.quit()

if __name__ == "__main__":
    main()