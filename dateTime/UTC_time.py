from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime() # 현재 날짜 및 시간 정보를 가져옴

print("Local datetime:", now.toString(Qt.ISODate)) # 현재 지역의 시간을 ISO 포맷을 사용하여 문자열로 출력. 시간은 T로 구분함
print("Universal datetime:", now.toUTC().toString(Qt.ISODate)) # 현재 UTC 표준시를 ISO 포맷을 사용하여 문자열로 출력

print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc())) # 현재 지역 시간과 UTC 표준시와의 초 단위 차이를 출력