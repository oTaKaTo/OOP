import math
enter_hr,enter_min,out_hr,out_min = [int(e) for e in input().split()]
sum_min,sum_hr,app_hr = 0,0,0
price = 0
sum_min += (out_hr-enter_hr)*60
if out_min >= enter_min:
    sum_min += out_min-enter_min
else:
    sum_min += enter_min-out_min
app_hr = sum_min/60
app_hr = math.ceil(app_hr)
if sum_min <= 15:
    pass
elif app_hr < 4 :
    price += app_hr*10
elif app_hr > 6 :
    price = 200
else:
    price = 30 + (app_hr-3)*20

print(price)