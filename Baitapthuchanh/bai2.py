# Bài 2: Ghi đoạn văn bản vào tập tin và hiển thị lại

ten_tap_tin = input("Nhập tên tập tin: ")
van_ban = input("Nhập đoạn văn bản: ")

with open(ten_tap_tin, "w", encoding="utf-8") as tep:
    tep.write(van_ban)

print("Nội dung vừa ghi:")
with open(ten_tap_tin, "r", encoding="utf-8") as tep:
    print(tep.read())
