#Chương trình Đổi phút thành giờ và phút ( đã biết làm )
#1 giờ = 60p
#1p = 60s
print("Chương trình đổi phút thành giờ và phút") 
print("======================================")
so_phut = int(input("Nhập số phút của bạn vào : ")) #nhập 250
print("======================================")
print('')
#========================================
so_gio = so_phut // 60 #(250 // 60)
so_Phut = so_phut % 60 #(250 % 60)
#========================================
print('')
print("Số giờ : ",so_gio)
print("sô phút : ",so_Phut)