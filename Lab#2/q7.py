"""
จากโปรแกรมในข้อ 7 ให้เขียนฟังก์ชัน เพิ่มเติมเป็น date_diff
– รับข้อมูลในรูปแบบ “dd-mm-yyyy” เช่น

date_diff(“1-1-2018”, “1-1-2020”) จะได้ 731 วัน
date_diff(“25-12-1999”, “9-3-2000”) จะได้ 76 วัน
– ให้เขียนฟังก์ชัน day_in_year โดยจะส่งค่าจํานวนวันของปี (365 หรือ 366) โดยรับข้อมูลเป็น ปี
– ส่งคืนข้อมูลเป็นจํานวนวันตั้งแต่วันที่แรก จนถึงวันที่สอง โดยรวมทั้ง 2 วันนั้นเข้าไปด้วย
– ให้สมมติว่าวันแรก จะต้องมาก่อนวันที่สองเสมอ ดังนั้นไม่ต้องตรวจสอบ
"""

day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_of_year(day, month, year):
    day_of_years = 0
    if is_leap(year):
        day_in_month[2] += 1
    else:
        if month == 2 and day == 29:
            return -1
    day_of_years = sum([day_in_month[d] for d in range(1,month)]) + day
    return day_of_years


print(day_of_year(1,2,2021))
