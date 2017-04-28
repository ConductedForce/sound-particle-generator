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
    #piano
    c3 = pygame.mixer.Sound('input\c3.wav')
    c4 = pygame.mixer.Sound('input\c4.wav')
    c5 = pygame.mixer.Sound('input\c5.wav')
    c6 = pygame.mixer.Sound('input\c6.wav')
    c7 = pygame.mixer.Sound('input\c7.wav')
    c8 = pygame.mixer.Sound('input\c8.wav')
    '''
    #guitar
    gh3 = pygame.mixer.Sound('input\gh3.wav')
    gh4 = pygame.mixer.Sound('input\gh4.wav')
    gn3 = pygame.mixer.Sound('input\gn3.wav')
    gn4 = pygame.mixer.Sound('input\gn4.wav')
    gn5 = pygame.mixer.Sound('input\gn5.wav')
    gp3 = pygame.mixer.Sound('input\gp3.wav')
    gp4 = pygame.mixer.Sound('input\gp4.wav')
    gs3 = pygame.mixer.Sound('input\gs3.wav')
    gs4 = pygame.mixer.Sound('input\gs4.wav')
    '''
    #better guitar
    A = pygame.mixer.Sound('input\A.aif')
    B = pygame.mixer.Sound('input\B.aif')
    D = pygame.mixer.Sound('input\D.aif')
    E = pygame.mixer.Sound('input\E.aif')
    G = pygame.mixer.Sound('input\G.aif')

    #guitar 
    g1 = pygame.mixer.Sound('input\g1.wav')
    g2 = pygame.mixer.Sound('input\g2.wav')
    g3 = pygame.mixer.Sound('input\g3.wav')
    g4 = pygame.mixer.Sound('input\g4.wav')
    g5 = pygame.mixer.Sound('input\g5.wav')
    g6 = pygame.mixer.Sound('input\g6.wav')

except:
    raise UserWarning("Could not load or play soundfiles in 'data' folder :-(")



def input(event):
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

       
if __name__ == "__main__":
    input()