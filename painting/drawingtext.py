import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.text = "햇빛이 선명하게\n 나뭇잎을 핥고 있었다."

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Drawing text')
        self.show()
    
    def paintEvent(self, event): # 재정의

        # QPainter의 모든 작동은 begin()과 end() 사이에서 일어난다.
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):

        # 펜(색) 및 폰트 지정, 위치 조정
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('굴림', 15))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())