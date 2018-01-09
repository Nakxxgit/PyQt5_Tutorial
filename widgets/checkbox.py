import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self) # Show title 이름을 가진 체크박스 생성
        cb.move(20 ,20)
        cb.toggle() # 체크된 상태로 전환
        cb.stateChanged.connect(self.changeTitle) # 체크박스 signal을 changeTitle 함수에 연결

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state): # 체크 여부는 state에 저장. 체크 여부에 따라 창 이름을 변경
    
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     sys.exit(app.exec_())