import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel, QFileDialog
import PyQt5.QtMultimedia as M 
import pwindow

import waveform as wvf

#This class works with the GUI
class StartGui(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = pwindow.Ui_MainWindow()
        self.ui.setupUi(self)
    
    ##############################
    # All action methods go here
    ##############################

    def exit(self, MainWindow):
        sys.exit(0)

    #Selecting file
    def selectFile(self, MainWindow):
        text, ok = QInputDialog.getText(self, 'File selection', 
            'Enter a wav file to play:')
        
        if ok:
            self.file = text

    #Playing file
    def run(self, MainWindow):
        M.QSound.play(self.file)
    
    def playFile(self, MainWindow):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print (fileName)
            sound_file = fileName
            M.QSound.play(sound_file)
            #label = QLabel(sound_file)
            #label.show()

    #Plot of the file
    def plot(self, MainWindow):
        window = wvf.LiveFFTWidget()