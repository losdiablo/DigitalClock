import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                             QWidget,QVBoxLayout,QVBoxLayout,
                             QGridLayout,QPushButton,QCheckBox,
                             QRadioButton,QButtonGroup,QLineEdit,QHBoxLayout)
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase
from PyQt5.QtCore import Qt,QTime,QTimer

class DigitalClock(QWidget):
  def __init__(self ):
    super().__init__()
    self.time_lable=QLabel(self)
    self.timer=QTimer(self)
    # self.setWindowIcon(QIcon("miniProjects/guiShit/Icon.jpg"))
    self.initUI()
  def initUI(self):
    self.setWindowTitle("Digital clock !")
    self.setGeometry(600,400,300,100)
    
    vbox=QVBoxLayout()
    vbox.addWidget(self.time_lable)
    self.setLayout(vbox)
    self.time_lable.setAlignment(Qt.AlignCenter)
    
    self.time_lable.setStyleSheet("font-size:150px;"
                                  "color:hsl(111,100%,50%);")
    self.setStyleSheet("background-color:black;")
    
    font_id=QFontDatabase.addApplicationFont("D:/WebS/miniProjects/DigitalClock/DS-DIGIT.TTF")
    font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
    my_font=QFont(font_family,150)
    self.time_lable.setFont(my_font)
    self.timer.timeout.connect(self.update_time)
    self.timer.start(1000)
    self.update_time()
    
        
  def update_time(self):
    current_time=QTime.currentTime().toString("hh:mm:ss AP")
    self.time_lable.setText(current_time)

if __name__=="__main__":
    app=QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())    
     
