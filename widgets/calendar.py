import sys
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication, QVBoxLayout
from PyQt5.QtCore import QDate

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self) # Calendar 생성
        cal.setGridVisible(True) # 격자 표시
        cal.clicked[QDate].connect(self.showDate) # Calendar 클릭 신호를 showDate에 연결

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date): # 신호에 담긴 값을 문자열 형태로 출력
        
        self.lbl.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())