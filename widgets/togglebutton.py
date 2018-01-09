import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0) # 기본 색 검정

        redb = QPushButton('Red', self) # 버튼 생성 후 체크 가능하게 설정
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor) # 클릭 여부를 boolean 값으로 신호 전달

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):

        source = self.sender() # 전송된 신호의 정보를 가져옴

        if pressed: # 눌렸을 경우 val를 255로 설정
            val = 255
        else: val = 0

        if source.text() == "Red": # 해당 색의 RGB 값을 val로 설정
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())

if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     sys.exit(app.exec_())