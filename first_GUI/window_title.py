import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv) # QApplication 객체 생성.
    
    w = QWidget() # 인터페이스 객체인 Widget 생성
    w.resize(250, 150) # 사이즈 조절
    w.move(300, 300) # 위치 조절
    w.setWindowTitle('Hello World') # 창 이름 설정
    w.show() # 위젯 w를 화면에 표시

    sys.exit(app.exec_()) # 앱이 끝나는 경우(메인 루프 종료) sys.exit을 통해 확실히 종료해준다.