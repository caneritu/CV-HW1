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
        self.inputLoaded = False
        self.targetLoaded = False
        self.initUI()

    def openInputImage(self):
        # This function is called when the user clicks File->Input Image.

        '''pic_name = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.gif)")
        input_pic.setPixmap(QPixmap(pic_name[0]))'''

        pic_name = "color2.png"
        input_pic = QLabel()
        self.vbox1.addWidget(input_pic)
        input_pic.setPixmap(QPixmap(pic_name))

        img = cv2.imread(pic_name, cv2.IMREAD_COLOR)

        histograms = self.calcHistogram(img)

        hist_plot = PlotCanvas(histograms[1:][:], width=5, height=4)

        self.vbox1.addWidget(hist_plot)

        self.inputLoaded = True


    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.

        pic_name = "color1.png"
        target_pic = QLabel()
        self.vbox2.addWidget(target_pic)
        target_pic.setPixmap(QPixmap(pic_name))

        img = cv2.imread(pic_name, cv2.IMREAD_COLOR)

        histograms = self.calcHistogram(img)

        hist_plot = PlotCanvas(histograms[1:][:], width=5, height=4)

        self.vbox2.addWidget(hist_plot)

        self.targetLoaded = True

    def exitdeneme(self):
        qApp.quit()

    def initUI(self):

        self.setGeometry(300, 100, 1200, 800)
        self.setWindowTitle('Histogram Equalization')

        self.setCentralWidget(QWidget(self))

        self.hbox = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox3 = QVBoxLayout()

        input_box = QLabel()
        target_box = QLabel()
        result_box = QLabel()

        input_box.setText("Input")
        target_box.setText("Target")
        result_box.setText("Result")

        self.vbox1.addWidget(input_box)
        self.vbox2.addWidget(target_box)
        self.vbox3.addWidget(result_box)

        self.hbox.addLayout(self.vbox1)
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox2)
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox3)

        self.centralWidget().setLayout(self.hbox)

        menubar = self.menuBar()
        menu_file = menubar.addMenu('File')

        open_input = QAction('Open Input', self)
        open_input.triggered.connect(lambda: self.openInputImage())

        open_target = QAction('Open Target', self)
        open_target.triggered.connect(lambda: self.openTargetImage())

        exit_app = QAction('Exit', self)
        exit_app.triggered.connect(self.exitdeneme)

        histogram_equalize = QAction('Equalize Histogram', self)
        histogram_equalize.triggered.connect(lambda: self.histogramButtonClicked())

        menu_file.addAction(open_input)
        menu_file.addAction(open_target)
        menu_file.addAction(exit_app)

        self.toolbar = self.addToolBar('toolbar')
        self.toolbar.addAction(histogram_equalize)

        self.show()

    def histogramButtonClicked(self):
        '''target_pic = QLabel()
        self.vbox3.addWidget(target_pic)
        target_pic.setPixmap(QPixmap("color2.png"))'''

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        if not self.inputLoaded and not self.targetLoaded:
            # Error: "First load input and target images" in MessageBox
            msg.setText("Error: First load input and target images")
            msg.exec_()
        elif not self.inputLoaded:
            # Error: "Load input image" in MessageBox
            msg.setText("Error: Load input image")
            msg.exec_()
        elif not self.targetLoaded:
            # Error: "Load target image" in MessageBox
            msg.setText("Error: Load target image")
            msg.exec_()


    def calcHistogram(self, I):
        # Calculate histogram
        x = np.row_stack((np.arange(256), np.zeros((3, 256), dtype=int)))
        # first row is 0,1,2,....255
        # other rows are for red, green and blue

        for i in range(len(I[:])):
            for j in range(len(I[0])):
                for r in range(len(I[0][0])):
                    x[r+1][I[i][j][r]] += 1
        return x


class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        '''self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)'''
        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        ax1 = self.figure.add_subplot(511)
        ax1.plot(hist[0], 'r-')

        ax2 = self.figure.add_subplot(513)
        ax2.plot(hist[1], 'g-')

        ax3 = self.figure.add_subplot(515)
        ax3.plot(hist[2], 'b-')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = App()
    sys.exit(app.exec_())