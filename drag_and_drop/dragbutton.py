import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton): # 기능 재정의를 위해 QPushButton 상속

    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton: # 마우스 오른쪽 버튼으로만 버튼 위치 조정 가능
            return

        mimeData = QMimeData()

        # QDrag 생성. MIME 기반 데이터 교환. 참고 링크: http://doc.qt.io/qt-5/examples-draganddrop.html
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e): # 버튼 클릭시 콘솔에 press 출력

        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        
        e.accept()

    def dropEvent(self, e):
        
        # 드랍 위치로 버튼 위치 재조정
        position = e.pos()
        self.button.move(position)

        # 드랍 시 action 설정
        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()