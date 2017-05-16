'''
Project 3
Abel, Joseph, Brandon
Abel = Particles.py, pathMap.py
Brandon = main.py, points.py, pwindow.py
Joseph = proj3keyboardinput.py, liveFile.py, liveMic.py


main.py
Allows operation of 3 input schemes and renders them appropiately
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel, QFileDialog
#import PyQt5.QtMultimedia as M 
import gui.pwindow as pwin
import pygame

import input.liveFile as fileb
import input.liveMic as micb
import input.proj3keyboardinput as keyb
import render.particles as ren
import analysis.points as sa
import random


def key():
    points = []
    #pygame.init()
    clock = pygame.time.Clock()
    exitflag = False
    data = clock
    points = sa.create(data) # analysis system # point generator
    activeRender = ren.Render()
    activeRender.make()
    pathList = activeRender.readPath(points)
    freq = 499
    while not exitflag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitflag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitflag = True
                freq = keyb.input(event) # input system

        #main loop code
        # analysis system
        activeRender.draw(points, pathList, freq) # draw system
        
        pygame.display.flip()
        clock.tick(80)
    pygame.quit()

def mic():
    clock = pygame.time.Clock()
    exitflag = False
    
    
    micO = micb.mic() #create fileSound object
    activeRender = ren.Render() #create render object
    activeRender.make() #generate particles
    
    test = 1
    while not exitflag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitflag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitflag = True
                
        
        #main loop code
        data,rate = micO.getMicChunkData() # input system
        freq = sa.analyze(data, rate)
        if test == 1:
            points = sa.create(data) # analysis system
            test += 1
            pathList = activeRender.readPath(points)
        activeRender.draw(points, pathList, freq) # draw system
        
        pygame.display.flip()
        clock.tick(rate)
    pygame.quit()

def file():
    clock = pygame.time.Clock()
    exitflag = False
    
    
    fileO = fileb.file() #create mic object
    activeRender = ren.Render() #create render object
    activeRender.make() #generate particles
    
    
    
    test = 1
    while not exitflag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitflag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitflag = True
                

        #main loop code
        data, rate = fileO.getFileChunkData() # input system
        freq = sa.analyze(data, rate)
        if test == 1:
            points = sa.create(data) # analysis system
            test += 1
            pathList = activeRender.readPath(points)
        activeRender.draw(points, pathList, freq) # draw system
        
        pygame.display.flip()
        clock.tick(rate)
    pygame.quit()

#a gui
class TheGui(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = pwin.Ui_MainWindow()
        self.ui.setupUi(self)

    #gui methods
    def live(self, MainWindow):
        mic()

    def file(self, MainWindow):
        file()
    
    def keyboard(self, MainWindow):
        key()

# main method
def main():
    app = QApplication(sys.argv)
    mainWindow = TheGui()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()