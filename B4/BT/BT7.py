# Bài 7 - Kiểm tra số chẵn lẻ
a = int(input("Nhập giá trị a : ")) #nhập giá trị chia hết cho 2 ví dụ 18
if a % 2 == 0: #Điều kiện nếu a chia hết cho 2 ( chẵn)
    print("Số chặn")
else: #nếu số không chia hết cho 2 mà dư 1 số sẽ là lẻ.
    print("số lẻ")