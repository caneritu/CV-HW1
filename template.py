import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog, qApp, QHBoxLayout  # QHBOXLAYOUT for trying only
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
        # You can define other things in here
        self.initUI()

    def openInputImage(self):
        # This function is called when the user clicks File->Input Image.
        input_pic = QLabel()
        self.vbox1.addWidget(input_pic)
        input_pic.setPixmap(QPixmap("color1.png"))


    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.
        target_pic = QLabel()
        self.vbox2.addWidget(target_pic)
        target_pic.setPixmap(QPixmap("color2.png"))

    def exitdeneme(self):
        qApp.quit()

    def initUI(self):

        self.setGeometry(300, 300, 600, 450)
        self.setWindowTitle('Histogram Equalization')



        self.setCentralWidget(QWidget(self))
        '''grid = QGridLayout()
        self.centralWidget().setLayout(grid)'''

        self.hbox = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox3 = QVBoxLayout()

        input_box = QLabel()
        target_box = QLabel()
        result_box = QLabel()

        #input_pic = QLabel()
        #target_pic = QLabel()
        result_pic = QLabel()

        input_box.setText("input")
        target_box.setText("target")
        result_box.setText("result")

        self.vbox1.addWidget(input_box)
        #self.vbox1.addWidget(input_pic)

        self.vbox2.addWidget(target_box)
        #self.vbox2.addWidget(target_pic)

        self.vbox3.addWidget(result_box)
        self.vbox3.addWidget(result_pic)

        self.hbox.addLayout(self.vbox1)

        self.hbox.addLayout(self.vbox2)

        self.hbox.addLayout(self.vbox3)

        self.centralWidget().setLayout(self.hbox)

        '''input_box.setAlignment(Qt.AlignLeft)
        target_box.setAlignment(Qt.AlignCenter)
        result_box.setAlignment(Qt.AlignRight)
        '''

        '''grid.addWidget(input_box, 0, 1, 1, 1)
        grid.addWidget(target_box, 0, 2, 1, 1)
        grid.addWidget(result_box, 0, 3, 1, 1)'''

        # Write GUI initialization code

        menubar = self.menuBar()
        menu_file = menubar.addMenu('File')

        open_input = QAction('Open Input', self)
        open_input.triggered.connect(lambda: self.openInputImage())

        open_target = QAction('Open Target', self)
        open_target.triggered.connect(lambda: self.openTargetImage())

        exit_app = QAction('Exit', self)
        exit_app.triggered.connect(self.exitdeneme)

        histogram_equalize = QAction('Equalize Histogram', self)
        histogram_equalize.triggered.connect(self.histogramButtonClicked())

        menu_file.addAction(open_input)
        menu_file.addAction(open_target)
        menu_file.addAction(exit_app)

        self.toolbar = self.addToolBar('toolbar')
        self.toolbar.addAction(histogram_equalize)

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