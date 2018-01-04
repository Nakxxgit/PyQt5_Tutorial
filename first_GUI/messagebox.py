import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QApplication

class Example(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, event): # X 버튼을 누를 때 실행되는 closeEvent() 수정을 위해 재정의

        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 새로운 질문 메시지박스 생성. 소속 위젯, 타이틀바에 들어갈 문자열, 내용에 들어갈 문자열, 나타낼 버튼 종류, 기본 선택지 순으로 인자를 준다.

        # 위에서 반환된 응답값에 따라 event에 대한 행동 결정
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())