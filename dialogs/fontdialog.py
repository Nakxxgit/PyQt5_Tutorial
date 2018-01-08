import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) # 버튼 크기 고정

        btn.move(20, 20)

        vbox.addWidget(btn)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):

        font, ok = QFontDialog.getFont() # 새 창을 띄워 폰트 선택. 각 변수에는 폰트 정보가 담긴 클래스와, 확인 버튼 클릭 여부를 저장.

        if ok: # 확인 버튼을 눌렀을 경우 해당 폰트 업데이트
            self.lbl.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())