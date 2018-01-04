import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        # 메뉴바, 툴바, 사용자정의 단축키 등에 쓰일 기능 클래스 QAction. 사용할 아이콘, 이름, 소속될 위젯 순으로 인자가 주어졌다.
        # QString의 특징으로, 앞에 엠퍼샌드('&')가 있으면 바로가기가 자동생성된다.
        # 넣었을 경우와 넣지 않았을 경우의 차이는 프로그램 실행 후 키보드에서 Alt -> E 입력 시 알 수 있다.
        exitAct.setShortcut('Ctrl+Q') # 키보드 단축키 설정
        exitAct.setStatusTip('Exit application') # 설명 추가
        exitAct.triggered.connect(qApp.quit) # 눌렀을 경우 프로그램 종료

        self.statusBar

        menubar = self.menuBar() # 메뉴바 생성
        fileMenu = menubar.addMenu('&File') # File 메뉴 추가. 이번에도 마찬가지로 QString 기능에 의해 바로가기가 생성된다
        fileMenu.addAction(exitAct) # File 메뉴에 exitAct 기능 추가

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
