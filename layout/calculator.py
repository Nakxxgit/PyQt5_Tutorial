import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        grid = QGridLayout() # Grid layout 생성
        self.setLayout(grid) # main layout으로 지정

        names = ['Cls', 'Bck', '', 'Close', # 버튼 이름이 저장된 리스트
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions =  [(i, j) for i in range(5) for j in range(4)] # 5 * 4 개의 좌표 생성

        for position, name in zip(positions, names): # 각 좌표값과 이름에 대해 반복문 수행

            if name == '': # 비어있는 이름은 아무것도 수행하지 않고 넘어감
                continue
            button = QPushButton(name) # 주어진 이름으로 버튼 생성
            grid.addWidget(button, *position) # 버튼을 주어진 좌표값 위치에 추가

        self.move(300, 150) # 위젯 크기는 Grid layout을 쓸 때 버튼 위치에 대해 자동으로 조정되기 떄문에 Qwidget.move()로 창 위치만 지정해주면 됨
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())