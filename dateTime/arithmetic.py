from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

'''
QDateTime.addSecs(n): n초만큼 더함
QDateTime.addDays(n): n일만큼 더함
QDateTime.addMonths(n): n달만큼 더함
QDateTime.addYears(n): n년만큼 더함
'''

print("Today", now.toString(Qt.ISODate))
print("Adding 12 days:", now.addDays(12).toString(Qt.ISODate))
print("Subtracting 22 days:", now.addDays(-22).toString(Qt.ISODate))

print("Adding 50 seconds:", now.addSecs(50).toString(Qt.ISODate))
print("Adding 3 months:", now.addMonths(3).toString(Qt.ISODate))
print("Adding 12 years:", now.addYears(12).toString(Qt.ISODate))