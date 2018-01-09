import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)

        # 칸마다 경계를 나누기 위해 StyledPanel 사용
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottomright = QFrame(self)
        bottomright.setFrameShape(QFrame.StyledPanel)

        bottomleft = QFrame(self)
        bottomleft.setFrameShape(QFrame.StyledPanel)

        # 수평 Splitter 생성, 두 개의 프레임 추가
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(bottomleft)
        splitter2.addWidget(bottomright)

        # 수직 Splitter 생성, 두 개의 수평 Splitter 추가 
        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)

        hbox.addWidget(splitter3)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())