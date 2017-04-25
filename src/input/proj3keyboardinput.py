'''
Implements mixer to play sound files, sounds can be mapped to keyboard input
Necessary to have sounds files in same file directory
Links to sound libraries:
http://www.findsounds.com/
http://soundcavern.free.fr/guitar/
'''

import pygame,random, array
from pygame.locals import *

xmax = 1000    #width of window
ymax = 600     #height of window

# VVV Added part VVV
#pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.mixer.init(48000, -16, 1, 1024)
pygame.init()

fadeTime=1000
maxTime=0,1,10,100,1000
pygame.mixer.fadeout(fadeTime)

try:
    cymbals = pygame.mixer.Sound('cymbals.wav')  #load sound
    bitchin = pygame.mixer.Sound('bitchin.wav')  #load sound
    bassDrum = pygame.mixer.Sound('Bass drum.wav')
    kick = pygame.mixer.Sound('kickatbc.wav')
    hi = pygame.mixer.Sound('hi_tune_4.wav')

    #piano
    c3 = pygame.mixer.Sound('c3.wav')
    c4 = pygame.mixer.Sound('c4.wav')
    c5 = pygame.mixer.Sound('c5.wav')
    c6 = pygame.mixer.Sound('c6.wav')
    c7 = pygame.mixer.Sound('c7.wav')
    c8 = pygame.mixer.Sound('c8.wav')
    '''
    #guitar
    gh3 = pygame.mixer.Sound('gh3.wav')
    gh4 = pygame.mixer.Sound('gh4.wav')
    gn3 = pygame.mixer.Sound('gn3.wav')
    gn4 = pygame.mixer.Sound('gn4.wav')
    gn5 = pygame.mixer.Sound('gn5.wav')
    gp3 = pygame.mixer.Sound('gp3.wav')
    gp4 = pygame.mixer.Sound('gp4.wav')
    gs3 = pygame.mixer.Sound('gs3.wav')
    gs4 = pygame.mixer.Sound('gs4.wav')
    '''
    #better guitar
    A = pygame.mixer.Sound('A.aif')
    B = pygame.mixer.Sound('B.aif')
    D = pygame.mixer.Sound('D.aif')
    E = pygame.mixer.Sound('E.aif')
    G = pygame.mixer.Sound('G.aif')

    #guitar 
    g1 = pygame.mixer.Sound('g1.wav')
    g2 = pygame.mixer.Sound('g2.wav')
    g3 = pygame.mixer.Sound('g3.wav')
    g4 = pygame.mixer.Sound('g4.wav')
    g5 = pygame.mixer.Sound('g5.wav')
    g6 = pygame.mixer.Sound('g6.wav')

except:
    raise UserWarning("Could not load or play soundfiles in 'data' folder :-(")


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
                    g1.play()
                elif event.key == pygame.K_x:
                    g2.play()
                elif event.key == pygame.K_c:
                    g3.play()
                elif event.key == pygame.K_v:
                    g4.play()
                elif event.key == pygame.K_b:
                    g5.play()
                elif event.key == pygame.K_n:
                    g6.play()
                #paino
                elif event.key == pygame.K_q:
                    c3.play()
                elif event.key == pygame.K_w:
                    c4.play()
                elif event.key == pygame.K_e:
                    c5.play()
                elif event.key == pygame.K_r:
                    c6.play()
                elif event.key == pygame.K_t:
                    c7.play()
                elif event.key == pygame.K_y:
                    c8.play()
                #guitar
                elif event.key == pygame.K_a:
                    A.play()
                elif event.key == pygame.K_s:
                    B.play()
                elif event.key == pygame.K_d:
                    D.play()
                elif event.key == pygame.K_f:
                    E.play()
                elif event.key == pygame.K_g:
                    G.play()
                    '''
                elif event.key == pygame.K_h:
                    gp3.play()
                elif event.key == pygame.K_j:
                    gp4.play()
                elif event.key == pygame.K_k:
                    gs3.play()
                elif event.key == pygame.K_l:
                    gs4.play()

                    '''

        screen.fill(black)
        for p in particles:
            p.move()
            pygame.draw.circle(screen, p.col, (p.x, p.y), 5)

        pygame.display.flip()
        clock.tick(90)
    pygame.quit()

if __name__ == "__main__":
    main()