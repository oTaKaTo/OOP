"""
    ให้เขียนโปรแกรมเพื่อรับข้อมูล 1 บรรทัด ที่ประกอบด้วยจํานวนเต็มหลายจํานวน (คั่นด้วยช่องว่าง)
    ให้ส่งคืนว่ามีจํานวนที่เป็นลบกี่จํานวน โดยใช้ List comprehension
    ให้เขียนในฟังก์ชัน count_minus(str) แล้ว return เป็นคําตอบ
"""

int_set = [i for i in input().split()]

def count_minus_test(str):
    n = sum([1 if int(i) < 0 else 0 for i in str])
    return n


count_minus_test(int_set)
