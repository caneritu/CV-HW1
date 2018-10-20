import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog, qApp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import cv2

##########################################
## Do not forget to delete "return NotImplementedError"
## while implementing a function
########################################

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
     #   self.initUI()


        self.title = 'Histogram Equalization'
        # You can define other things in here
        self.initUI()

    def openInputImage(self):
        # This function is called when the user clicks File->Input Image.
        return NotImplementedError

    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.
        return NotImplementedError

    def exitdeneme(self):
        qApp.quit()

    def initUI(self):

        self.setGeometry(300, 300, 600, 450)
        self.setWindowTitle('Histogram Equalization')

        menubar = self.menuBar()
        menu_file = menubar.addMenu('File')

        open_input = QAction('Open Input', self)
        open_input.triggered.connect(self.openInputImage())

        open_target = QAction('Open Target', self)
        open_target.triggered.connect(self.openTargetImage())

        exit_app = QAction('Exit', self)
        exit_app.triggered.connect(self.exitdeneme)

        histogram_equalize = QAction('Equalize Histogram', self)
        histogram_equalize.triggered.connect(self.histogramButtonClicked())

        menu_file.addAction(open_input)
        menu_file.addAction(open_target)
        menu_file.addAction(exit_app)


        self.toolbar = self.addToolBar('toolbar')
        self.toolbar.addAction(histogram_equalize)

        # Write GUI initialization code

        self.show()

    def histogramButtonClicked(self):
        return NotImplementedError
        if not self.inputLoaded and not self.targetLoaded:
            # Error: "First load input and target images" in MessageBox
            return NotImplementedError
        if not self.inputLoaded:
            # Error: "Load input image" in MessageBox
            return NotImplementedError
        elif not self.targetLoaded:
            # Error: "Load target image" in MessageBox
            return NotImplementedError

    def calcHistogram(self, I):
        # Calculate histogram
        return NotImplementedError

class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        return NotImplementedError
        # Init Canvas
        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        return NotImplementedError
        # Plot histogram

        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = App()
    sys.exit(app.exec_())