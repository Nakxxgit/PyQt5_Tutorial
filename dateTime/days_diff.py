from PyQt5.QtCore import QDate

# a.daysTo(b): a로부터 b까지의 일수를 구함

PEPERO1 = QDate(2017, 11, 11)
PEPERO2 = QDate(2018, 11, 11)
now = QDate.currentDate()

print(PEPERO1.daysTo(now), "days have passed since last 11/11")
print("There are {0} days until next 11/11".format(now.daysTo(PEPERO2)))