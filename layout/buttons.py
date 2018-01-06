import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton("Ok") # 버튼 생성
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout() # Horizontal Boxlayout 생성 
        hbox.addStretch(1) # Stretchable한 빈 공간을 Horizontal Boxlayout에 추가
        hbox.addWidget(okButton) # ok 버튼을 Horizontal Boxlayout에 추가
        hbox.addWidget(cancelButton) # Cancel 버튼을 Horizontal Boxlayout에 추가
        # 창 크기에 맞게 늘어나는 빈 공간, ok버튼, cancel버튼 순서대로 hbox에 추가되었기 때문에 ok버튼과 cancel 버튼이 오른쪽 끝에 유지된다.

        vbox = QVBoxLayout() # Vertical Boxlayout 생성
        vbox.addStretch(1) # Stetchabel Space 추가
        vbox.addLayout(hbox) # hbox 추가
        # 빈 공간, hbox 순으로 vbox에 추가되었기 때문에, 최종적으로 ok 버튼과 cancel 버튼은 오른쪽 아래에 위치가 고정된다.

        self.setLayout(vbox) # main layout 설정

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())