#โปรแกรมคำนวณหาค่าเฉลี่ยของตัวเลขที่ป้อนไปโดยกำหนดได้ว่าป้อนกี่ตัว

"""
names = []
for i in range(3):
    name = str(input('ใส่ชื่อนักเรียน'))
    names.append(name)
print(names)
"""

names = []
num = int(input("จำนวนตัวเลขที่ต้องการป้อน :"))
for i in range(num):
    num = int(input('กรุณาใส่ตัวเลข : '))
    names.append(num)
r = sum(names)/len(names)
print(names)
print(f'ค่าเฉลี่ย{r}')