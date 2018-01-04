import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget): # QWidget을 상속하는 클래스 Example 생성

    def __init__(self):
        super().__init__() #중복 상속을 막기 위해 부모 클래스의 생성자 실행
        self.initUI() # GUI 생성

    def initUI(self):

        self.setGeometry(300, 300, 300, 220) # 창의 위치 및 크기 설정
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('./Icon/ex.png')) # 해당 파일을 QIcon 객체로 생성 후 창의 아이콘으로 설정

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())