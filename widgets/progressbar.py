import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self) # progressbar 생성
        self.pbar.setGeometry(30, 40, 200, 25)
        
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer() # 타이머 생성
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowFilePath('QProhressBar')
        self.show()

    def timerEvent(self, e):

        if self.step >= 100: #progressbar 진행 단계가 100 이상일 경우, 타이머 정지 후 버튼 text를 Finished로 변경

            self.timer.stop()
            self.btn.setText('Finished')
            return
        
        # progressbar 진행 단계를 1씩 추가 및 표시
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive(): # 타이머가 실행 중일 때 버튼을 누르면 타이머 중지, 그리고 버튼 text를 Start로 변경
            self.timer.stop()
            self.btn.setText('Start')
        else: # 정지 중일 때 버튼을 누르면 타이머 진행, 버튼 text를 Stop으로 변경
            self.timer.start(100, self) # 타이머 시작. 인자는 타이머 시간, 그리고 값을 전달할 객체
            self.btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())