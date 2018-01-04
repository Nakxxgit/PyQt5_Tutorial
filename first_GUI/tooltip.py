import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10)) # 글꼴 설정

        self.setToolTip('This is a <b>QWidget</b> widget') # 툴팁 생성, html 태그 사용 가능

        btn = QPushButton('Button', self) # 버튼 생성
        btn.setToolTip('This is a <b>QPushButton</b> widget') # 버튼에 대한 툴팁 생성
        btn.resize(btn.sizeHint()) # 버튼 사이즈 조절
        btn.move(50, 50) # 버튼 위치 조절

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())