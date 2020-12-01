import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(100, 100, 700, 500)
        
        self.title = "Image Editor"
        self.setWindowTitle(self.title)

        layout = QGridLayout()

        self.importBtn = QPushButton("Import Photo to Edit")
        self.importBtn.clicked.connect(self.getfile)
        self.importBtn.setStyleSheet(
            "background-color: white;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: gray;"
            "font: bold 12px;"
            "max-width: 10em;"
            "padding: 6px;"
        )

        self.exportBtn = QPushButton("Export Edited Photo")
        self.exportBtn.clicked.connect(self.savefile)
        self.exportBtn.setStyleSheet(
            "background-color: white;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: gray;"
            "font: bold 12px;"
            "max-width: 10em;"
            "padding: 6px;"
        )
        
        layout.addWidget(self.importBtn, 0,0)
        layout.addWidget(self.exportBtn, 0,1)
        
        self.imgLabel = QLabel()
        self.imgLabel.setStyleSheet(
            "background-color: white;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: gray;"
            "max-width: 300;"
            "max-height: 400;"
            "min-width: 300;"
            "min-height: 400;"
            "padding: 6px;"
        )
        self.imgLabel.resize(600, 300)
        layout.addWidget(self.imgLabel, 1,2,6,-1)

        self.satSliderLabel = QLabel("Saturation")
        self.satSliderLabel.setStyleSheet(
            "font: bold 12px;"
            "width: 70;"
            "padding: 6px;"
        )
        self.satSlider = QSlider(Qt.Horizontal)
        self.satSlider.setStyleSheet(
            "background-color: white;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: gray;"
            "font: bold 12px;"
            "max-width: 315px;"
        )
        layout.addWidget(self.satSliderLabel, 1,0,1,0)
        layout.addWidget(self.satSlider, 2,0,1,0)


        self.sharpSliderLabel = QLabel("Sharpness")
        self.sharpSliderLabel.setStyleSheet(
            "font: bold 12px;"
            "width: 70;"
            "padding: 6px;"
        )
        self.sharpSlider = QSlider(Qt.Horizontal)
        self.sharpSlider.setStyleSheet(
            "background-color: white;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: gray;"
            "font: bold 12px;"
            "max-width: 315px;"
        )
        layout.addWidget(self.sharpSliderLabel, 3,0,1,0)
        layout.addWidget(self.sharpSlider, 4,0,1,0)

        self.contrastSliderLabel = QLabel("Contrast")
        self.contrastSliderLabel.setStyleSheet(
            "font: bold 12px;"
            "width: 70;"
            "padding: 6px;"
        )
        self.contrastSlider = QSlider(Qt.Horizontal)
        self.contrastSlider.setStyleSheet(
            "background-color: white;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: gray;"
            "font: bold 12px;"
            "max-width: 315px;"
        )
        
        layout.addWidget(self.contrastSliderLabel, 5,0)
        layout.addWidget(self.contrastSlider, 6,0,1,0)

        self.spacerLabel = QLabel()
        self.spacerLabel.setStyleSheet(
            "height: 10px;"
        )
        layout.addWidget(self.spacerLabel, 7,0)
		
        self.setLayout(layout)
        self.setWindowTitle("Insta Photo Editor!")

        
    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Save file', 
            'c:\\',"Image files (*.jpg *.gif)")
        
        if fname:
            pixmap = QPixmap(fname)
            self.imgLabel.setPixmap(pixmap)

    def savefile(self):
        print("Pretend this saves it")
        
def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()



#Slide for saturation
#Slide for sharpness
#Slide for contrast
#?? for size
#Radio for color/grayscale

        
#app = QApplication(sys.argv)
#app.setStyle('Fusion')

#window = MainWindow()
#layout = QVBoxLayout()

#window.setLayout(layout)
#window.show()
#sys.exit(app.exec_())
