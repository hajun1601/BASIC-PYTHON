"""Nhập tổng số giây.

Đổi thành:

Phút
Giây dư

Ví dụ

125

Kết quả:
2 phút
5 giây
"""
a = int(input("Nhập số phút :")) #Nhập 125
b = 60

phut = a // b
giay = a % b

print("Phút :",phut,"Phút")
print("Giây :",giay,"Giây")