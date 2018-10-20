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

        self.input_histograms = self.calcHistogram(img)

        hist_plot = PlotCanvas(self.input_histograms, width=5, height=4)

        self.vbox1.addWidget(hist_plot)

        self.inputLoaded = True


    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.

        pic_name = "color1.png"
        target_pic = QLabel()
        self.vbox2.addWidget(target_pic)
        target_pic.setPixmap(QPixmap(pic_name))

        img = cv2.imread(pic_name, cv2.IMREAD_COLOR)

        self.target_histograms = self.calcHistogram(img)

        hist_plot = PlotCanvas(self.target_histograms, width=5, height=4)

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
        input_box.setAlignment(Qt.AlignTop)
        target_box.setText("Target")
        target_box.setAlignment(Qt.AlignTop)
        result_box.setText("Result")
        result_box.setAlignment(Qt.AlignTop)

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

        cumulative_input_red = np.cumsum(self.input_histograms[0])
        cumulative_input_green = np.cumsum(self.input_histograms[1])
        cumulative_input_blue = np.cumsum(self.input_histograms[2])

        cumulative_target_red = np.cumsum(self.target_histograms[0])
        cumulative_target_green = np.cumsum(self.target_histograms[1])
        cumulative_target_blue = np.cumsum(self.target_histograms[2])

        LUT = np.zeros((256, 3))
        g_j = 0
        for g_i in range(255):
            while cumulative_target_red[g_j] < cumulative_input_red[g_i] and g_j < 255:
                g_j += 1
            LUT[g_i][0] = g_j
        g_j = 0
        for g_i in range(255):
            while cumulative_target_green[g_j] < cumulative_input_green[g_i] and g_j < 255:
                g_j += 1
            LUT[g_i][1] = g_j
        g_j = 0
        for g_i in range(255):
            while cumulative_target_blue[g_j] < cumulative_input_blue[g_i] and g_j < 255:
                g_j += 1
            LUT[g_i][2] = g_j

        pic_name = "color2.png"
        img = cv2.imread(pic_name, cv2.IMREAD_COLOR)

        for i in range(len(img[:])):
            for j in range(len(img[0])):
                for r in range(len(img[0][0])):
                    img[i][j][r] = LUT[img[i][j][r]][r]

        result_pic = QLabel()
        self.vbox3.addWidget(result_pic)
        cv2.imwrite("result.png", img)
        result_pic.setPixmap(QPixmap("result.png"))

        self.result_histograms = self.calcHistogram(img)

        hist_plot = PlotCanvas(self.result_histograms, width=5, height=4)

        self.vbox3.addWidget(hist_plot)



    def calcHistogram(self, I):
        # Calculate histogram
        x = np.row_stack((np.arange(256), np.zeros((3, 256), dtype=int)))
        # first row is 0,1,2,....255
        # other rows are for red, green and blue

        for i in range(len(I[:])):
            for j in range(len(I[0])):
                for r in range(len(I[0][0])):
                    x[r+1][I[i][j][r]] += 1
        return x[1:][:]


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