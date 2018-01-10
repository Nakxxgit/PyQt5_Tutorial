import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QApplication

class Button(QPushButton): # 기능 수정을 위해 QPushButton을 상속

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True) # 생성 시 드랍 이벤트 허용

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'): # plain text 데이터를 허용하도록 수정
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e):

        self.setText(e.mimeData().text()) # 드랍된 텍스트로 버튼 텍스트 변경

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        edit = QLineEdit('', self)
        edit.setDragEnabled(True) # 드래그 허용
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Simple drag and drop')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()