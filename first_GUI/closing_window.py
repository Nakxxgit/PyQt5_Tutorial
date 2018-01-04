import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):

        qbtn = QPushButton('Quit', self) # 버튼을 소속시킬 위젯을 두번째 인자로 줌
        qbtn.clicked.connect(QCoreApplication.instance().quit) # qbtn이 눌렸을 경우 메인루프와 관련된 기능을 포함하는 QCoreApplication의 quit으로 연결
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())