import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel, QFileDialog
#import PyQt5.QtMultimedia as M 
import gui.pwindow as pwin
import pygame

#import map.detector as dt
import input.proj3keyboardinput as keyb
#import render.particles.py as ren
#import points.pointMaker as pm
import map.points as point



def deploy():
    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        #main loop code
        keyb.main() # input system
        # analysis system
        # point generator
        #pon.draw()

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