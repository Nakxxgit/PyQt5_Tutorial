import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow): # 텍스트에딧 위젯을 메인 위젯으로 설정하기 위해 QMainWindow 상속

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('../Icon/open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+T')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home') # 첫 번째 문자열은 caption, 두 번째 문자열은 파일 탐색할 기본 위치

        if fname[0]: # 지정한 경로의 파일을 읽어와 텍스트에딧에 업데이트
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__  == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())