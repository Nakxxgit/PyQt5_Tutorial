import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        sld = QSlider(Qt.Horizontal, self) # 수평을 이루는 Slider 생성
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue) # 슬라이더의 값을 정수형으로 전달할 신호 연결

        self.label = QLabel(self) # 라벨 생성 후 기본 이미지 삽입
        self.label.setPixmap(QPixmap('../Icon/mute.png'))
        self.label.setGeometry(160, 20, 80, 80)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Qslider')
        self.show()

    def changeValue(self, value):
        
        if value == 0: # Slider로부터 전해지는 신호 값에 따라 이미지 교체
            self.label.setPixmap(QPixmap('../Icon/mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('../Icon/min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('../Icon/med.png'))
        else:
            self.label.setPixmap(QPixmap('../Icon/max.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())