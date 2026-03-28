# Bài 3: Tính tuổi từ năm sinh
import time

# Lấy năm hiện tại
x = time.localtime()
nam_hien_tai = x.tm_year

# Nhập vào năm sinh
nam_sinh = int(input("Nhập năm sinh của bạn: "))

# Tính tuổi
tuoi = nam_hien_tai - nam_sinh

# In ra tuổi
print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")