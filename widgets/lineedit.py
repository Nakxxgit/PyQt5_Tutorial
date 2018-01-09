import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel(self)
        qle = QLineEdit(self) # QLineEdit 생성

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged) # qle의 문자열 형태 신호를 onChanged()에 연결

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QlineEdit')
        self.show()

    def onChanged(self, text): # 전달된 문자열로 라벨의 텍스트 업데이트 및 길이에 맞게 라벨 크기 재조정

        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())