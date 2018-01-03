from PyQt5.QtCore import QDate, Qt

# 년, 월에 있는 날의 수를 출력해줌

now = QDate.currentDate()

d = QDate(1945, 5, 7)

print("Days in month:", d.daysInMonth())
print("Days in year:", d.daysInYear())