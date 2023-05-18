day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_of_year(day, month, year):
    if not(is_leap(year)) and month == 2 and day == 29:
        return -1
    day_of_years = sum([day_in_month[d] for d in range(1, month)]) + day + (1 if (is_leap(year) and month > 2) else 0)
    return day_of_years


def date_diff(date_1, date_2):
    day_diff = 0
    date_1 = date_1.split("-")
    date_2 = date_2.split("-")
    if int(date_2[2]) - int(date_1[2]) >= 1:
        for i in range(int(date_1[2]), int(date_2[2])):
            day_diff += day_in_year(i)
    day_diff += (day_of_year(int(date_2[0]), int(date_2[1]), int(date_2[2]))) - (day_of_year(int(date_1[0]), int(date_1[1]), int(date_1[2])))

    return day_diff + 1

def day_in_year(year) :
    return 366 if is_leap(year) else 365

print(date_diff("1-1-2018", "1-1-2020"))
print(date_diff("25-12-1999", "9-3-2000"))
