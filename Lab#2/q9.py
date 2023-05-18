"""
จากโปรแกรมในข้อ 8 ให้เขียนฟังก์ชัน date_diff เพิ่มเติม โดยให้มีการตรวจสอบ
– วันที่ต้องเป็นวันที่ถูกต้องของเดือนนั้นๆ
– เดือนต้องอยู่ระหว่าง 1-12
– เดือนกุมภาพันธ์ของปีที่มี Leap Year เท่านั้นที่จะมี 29 วันได้
– หากข้อมูล Input ผิดพลาด ให้ Return -1
"""

day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_of_year(day, month, year):
    if not (is_leap(year)) and month == 2 and day == 29:
        return -1
    day_of_years = sum([day_in_month[d] for d in range(1, month)]) + day + (1 if (is_leap(year) and month > 2) else 0)
    return day_of_years


def date_diff(date_1, date_2):
    day_diff = 0
    date_1 = date_1.split("-")
    date_2 = date_2.split("-")
    if error_check(date_1) or error_check(date_2):
        return -1

    if int(date_2[2]) - int(date_1[2]) >= 1:
        for i in range(int(date_1[2]), int(date_2[2])):
            day_diff += day_in_year(i)
    day_diff += (day_of_year(int(date_2[0]), int(date_2[1]), int(date_2[2]))) - (
        day_of_year(int(date_1[0]), int(date_1[1]), int(date_1[2])))

    return day_diff + 1


def day_in_year(year):
    return 366 if is_leap(year) else 365


def error_check(date_month):
    if not (is_leap(int(date_month[2]))) and int(date_month[1]) == 2 and int(date_month[0]) == 29 or not(1 <= int(date_month[1]) <= 12) or not(1 <= int(date_month[0]) <= day_in_month[int(date_month[1])]):
        return -1
    else:
        return 0


print(date_diff("32131231-3123-2018", "1-1-2020"))
print(date_diff("25-12-1999", "9-3-2000"))
