#Bài 6 - Đổi giây thành giờ phút giây (Chưa hiểu cách làm)
print("Chương trình này dùng để đổi giây thành giờ phút giây") #Chương trình in ra màn hình tiêu đề
sogio = int(input("Vui lòng nhập số giây : ")) #Nhập 3675
print("") #cách dòng nhìn cho dễ
gio = sogio // 3600 # in ra sẽ thành 1 giờ chia nguyên (3675 // 36000 ) ( 1 Giờ )
gio_giay = sogio % 3600 # in ra là 75 giây ( chia dư ) ( 3675 $ 3600 ) ( 75 Giây)
phut = gio_giay // 60 #75 chia cho 60 = 1 phút ( chia nguyên ) ( 75 // 60 )
giay = gio_giay % 60 # chia du là còn 15 giây ( chia dư ) ( 75 % 60)

print("")
print("Số giờ của bạn là : ",gio)
print("Số phút của bạn là : ",phut)
print("Số giây của bạn là : ",giay)
print("")