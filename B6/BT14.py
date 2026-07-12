"""Một ngày có 24 giờ.

Nhập tổng số giờ.

Hỏi đã trải qua:

Bao nhiêu ngày.
Còn dư bao nhiêu giờ.

Ví dụ

Nhập: 53

2 ngày
5 giờ
"""
a = int(input("Nhập số giờ : "))
b = 24

ngay = a // b
gio =  a % b
print("")
print("Số ngày : ",ngay,"Ngày")
print("Số giờ : ",gio,"Giờ")