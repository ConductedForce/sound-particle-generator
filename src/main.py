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


def key():
    points = []
    #pygame.init()
    clock = pygame.time.Clock()
    exitflag = False
    points = sa.create(data) # analysis system # point generator
    pathList = activeRender.readPath(points)
    activeRender = ren.Render()
    activeRender.make()
    while not exitflag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitflag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitflag = True
                keyb.input(event) # input system

        #main loop code
        # analysis system
        activeRender.draw(points) # draw system
        
        pygame.display.flip()
        clock.tick(80)
    pygame.quit()

def mic():
    clock = pygame.time.Clock()
    exitflag = False
    
    
    micO = micb.mic() #create fileSound object
    activeRender = ren.Render() #create render object
    activeRender.make() #generate particles
    
    data = micO.getMicChunkData() # input system
    points = sa.create(data) # analysis system
    pathList = activeRender.readPath(points)
    while not exitflag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitflag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitflag = True
                

        #main loop code
       
        activeRender.draw(points, pathList) # draw system
        
        pygame.display.flip()
        clock.tick(1)
    pygame.quit()

def file():
    clock = pygame.time.Clock()
    exitflag = False
    
    
    fileO = fileb.file() #create mic object
    activeRender = ren.Render() #create render object
    activeRender.make() #generate particles
    
    
    
    
    while not exitflag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitflag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitflag = True
                

        #main loop code
        data = fileO.getFileChunkData() # input system
        points = sa.create(data) # analysis system
        pathList = activeRender.readPath(points)
        activeRender.draw(points, pathList) # draw system
        
        pygame.display.flip()
        clock.tick(1)
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