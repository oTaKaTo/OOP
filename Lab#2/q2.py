'''
กําหนดให้ List x เก็บ String และตัวแปร c เก็บตัวอักษร
ให้สร้าง List d ที่เก็บจํานวนครั้งที่ตัวอักษรใน c ปรากฏในแต่ละ String ของ List x โดยใช้ List
comprehension
– เช่น x = [‘abba’, ‘babana’, ‘ann’]; c = ‘a’
– จะได้ d = [2, 3, 1]
ให้สร้างเป็น function count_char_in_string(x,c) แล้ว return เป็น List คําตอบ
'''

x = ['abba', 'babana', 'ann'];
c = 'a'


def count_char_in_string(x, c):
    d = [n.count(c) for n in x ]
    return d