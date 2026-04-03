# Bài 1: Đọc n dòng đầu tiên của một tập tin

ten_tap_tin = input("Nhập tên tập tin: ")
n = int(input("Nhập số dòng cần đọc: "))

with open(ten_tap_tin, "r", encoding="utf-8") as tep:
    for i in range(n):
        dong = tep.readline()
        if dong == "":
            break
        print(dong.strip())
