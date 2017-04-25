import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel, QFileDialog
#import PyQt5.QtMultimedia as M 
import gui.pwindow as pwin
import pygame

#import map.detector as dt
import input.proj3keyboardinput as keyb
import render.particles as ren
#import analysis. as sa
import map.points as pm



def deploy():
    points = []
    #pygame.init()
    clock = pygame.time.Clock()
    exitflag = False
    points = pm.create() # point generator
    activeRender = ren.Render()
    activeRender.make()
    while not exitflag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitflag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitflag = True

        #main loop code
        keyb.main() # input system
            # analysis system
        activeRender.draw(points) # draw system
        
        pygame.display.flip()
        clock.tick(80)
    pygame.quit()


#a gui
class TheGui(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = pwin.Ui_MainWindow()
        self.ui.setupUi(self)

    #gui methods
    def live(self, MainWindow):
        point.exitHamlet()

    def file(self, MainWindow):
        keyb.main()
    
    def keyboard(self, MainWindow):
        deploy()

# main method
def main():
    app = QApplication(sys.argv)
    mainWindow = TheGui()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()