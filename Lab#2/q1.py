'''
ให้เขียนโปรแกรมรับข้อมูล 1 บรรทัด ประกอบด้วยตัวเลข 1 หลัก จํานวนไม่เกิน 10 ตัว คั่นด้วยช่องว่าง
จากนั้นให้นําตัวเลขที่รับเข้ามาเรียงกัน และหาลําดับการเรียงที่ทําให้มีค่าน้อยที่สุด โดยต้องไม่ขึ้นต้นด้วย 0
Input : 9 4 6 2 คําตอบ 2469, Input : 3 0 8 1 3 3 คําตอบ : 103338
'''

num_set = [int(e) for e in input().split()]
num_set.sort()
if num_set[0] == 0: num_set[0], num_set[1] = num_set[1], num_set[0]
for i in num_set: print(i, end="")
