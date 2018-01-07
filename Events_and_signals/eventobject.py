import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x, y = 0, 0

        self.text = "x: {0}, y: {1}".format(x, y) # 화면에 좌표 표시할 형식 지정

        self.label = QLabel(self.text, self) # 라벨 생성
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True) # 마우스 위치 추적 설정

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e): # 마우스가 움직일 때, text에 새 위치를 저장해 화면에 표시

        x = e.x()
        y = e.y()

        text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(text) 

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())