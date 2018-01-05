import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self) # import 메뉴 생성
        impAct = QAction('Import mail', self) # import mail 액션 생성
        impMenu.addAction(impAct) # import mail 액션을 import 메뉴에 추가

        newAct = QAction('New', self) # new 액션 생성

        fileMenu.addAction(newAct) # file 메뉴에 new 액션 추가
        fileMenu.addMenu(impMenu) # file 메뉴에 import 메뉴를 서브메뉴로 추가

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())