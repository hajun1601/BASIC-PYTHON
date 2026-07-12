"""
Một thùng chứa được 24 chai.

Nhập số chai.

Hỏi:

Đóng được bao nhiêu thùng.
Còn dư bao nhiêu chai.

Ví dụ

Nhập: 85

Đóng được: 3 thùng
Dư: 13 chai
"""

a = int(input("Nhập số Thùng : ")) #85 Thùng
b = int(input("Nhập số Trai : ")) #24 Chaid

t1 = a // b
t2 = a % b

print("")
print("Đóng được :",t1,"Thùng")
print("Dư :",t2,"Dư")