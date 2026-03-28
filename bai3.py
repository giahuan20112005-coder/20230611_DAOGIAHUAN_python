# Bài 3: Tính tuổi từ năm sinh
import time
nam_sinh = int(input("Nhập vào năm sinh của bạn: "))
xu_ly_thoi_gian = time.localtime()
nam_hien_tai = xu_ly_thoi_gian[0]
tuoi = nam_hien_tai - nam_sinh
print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")
