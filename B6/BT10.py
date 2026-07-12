"""
Nhập tổng số phút.

Hãy đổi thành:

Bao nhiêu giờ
Còn dư bao nhiêu phút

Ví dụ

Nhập: 367

Kết quả:
6 giờ
7 phút
"""
a = int(input("Nhập số phút : ")) #Nhập 367
b = 60
c = a // b
d = a % b
print("")
print("Kết quả :")
print("Giờ  : ",c,"Giờ")
print("Phút : ",d,"Phút")