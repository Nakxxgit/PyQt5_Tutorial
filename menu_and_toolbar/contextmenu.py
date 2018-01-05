import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')
        self.show()
    
    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        print(cmenu.exec_(self.mapToGlobal(event.pos())))
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        # mapToGlobal(event.pos()): event.pos로 주어진 위젯 내 마우스포인터의 위치를 전체 디스플레이 내 위치로 변환해줌
        # cmenu.exec_(): 우클릭 시 나타는 팝업 중 주어진 위치와 일치하는 액션을 반환

        if action == quitAct: # Quit를 누를 경우 앱 종료
            qApp.quit()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())