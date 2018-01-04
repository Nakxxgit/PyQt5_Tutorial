from PyQt5.QtCore import QDateTime, Qt

'''
QDateTime.toSecsSinceEpoch(): 주어진 시간의 초 단위 유닉스 시간을 구함
QDateTime.fromSecsSinceEpoch(n): 1970년 1월 1일 00:00:00부터 n초만큼 지난 시간을 구함
'''

now = QDateTime.currentDateTime()

unix_time = now.toSecsSinceEpoch()
print(unix_time))

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.ISODate))