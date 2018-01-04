import sys 
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry() # 위젯 프레임 정보 반환
        cp = QDesktopWidget().availableGeometry().center() # 사용(표시)가능한 화면 위치 중 중앙을 반환
        qr.moveCenter(cp) # 위젯을 cp 위치로 이동
        self.move(qr.topLeft())

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())