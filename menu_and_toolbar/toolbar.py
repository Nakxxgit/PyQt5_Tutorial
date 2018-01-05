import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('./icon/exit.png'), 'Exit', self) # Exit 액션 생성
        exitAct.setShortcut('Ctrl+Q') # Exit 액션 단축키 설정
        exitAct.triggered.connect(qApp.quit) # Exit이 실행될 경우 앱 종료

        self.toolbar = self.addToolBar('Exit') # Exit 툴바 생성
        self.toolbar.addAction(exitAct) # Exit 액션을 추가

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())