import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')
        # 상태표시줄을 생성하기 위해 QtGui.QMainWindow 클래스의 statusBar() 호출. showMessage가 메시지를 표시한다.

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())