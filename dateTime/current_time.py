from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate() # QDate.currentDate()가 현재 날짜 정보 반환

print(now.toString(Qt.ISODate)) # ISO(국제 표준 날짜 형식) 포맷을 사용하여 문자열 형태로 출력
print(now.toString(Qt.DefaultLocaleLongDate)) # 기본 포맷을 사용하여 문자열 형태로 출력

datetime = QDateTime.currentDateTime() # QDateTime.currentDateTime()이 현재 날짜와 시간 정보 반환

print(datetime.toString()) # 현재 날짜와 시간을 문자열 형태로 출력

time = QTime.currentTime() # QTime.currentTime()이 현재 시간 정보 반환

print(time.toString(Qt.DefaultLocaleLongDate)) # 현재 시간을 문자열 형태로 출력