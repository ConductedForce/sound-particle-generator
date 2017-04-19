import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel, QFileDialog
#import PyQt5.QtMultimedia as M 
import gui.pwindow as pwin

#import map.detector as dt
import input.proj3keyboardinput as keyb
#import render.particles.py as ren
#import points.pointMaker as pm
import map.points as point

class TheGui(Q
def __init__(self, parent = None):
    QMainWindow.__init__(self, parent)
    self.ui = pwin.Ui_MainWindow()
    self.ui.setupUi(self)

# main method
def main(self):
    app = QApplication(sys.argv)
    mainWindow = __init__(self)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(self)


#gui methods
def live(self, MainWindow):
    point.exitHamlet()

def file(self, MainWindow):
    keyb.main()
    
def keyboard(self, MainWindow):
    deploy()






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
        keyb.main()
        point.exitHamlet()
        #pon.draw()