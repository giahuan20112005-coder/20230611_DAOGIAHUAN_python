# Bài 3: Tạo file demo_file1.txt và đọc nội dung

noi_dung = "Thuc \n hanh \n voi \n file\n IO\n"

# Tạo file và ghi nội dung
with open("demo_file1.txt", "w", encoding="utf-8") as tep:
    tep.write(noi_dung)

# a) In nội dung file trên một dòng
with open("demo_file1.txt", "r", encoding="utf-8") as tep:
    noi_dung_file = tep.read().replace("\n", " ")
    print("Nội dung trên một dòng:")
    print(noi_dung_file.strip())

# b) In nội dung file theo từng dòng
with open("demo_file1.txt", "r", encoding="utf-8") as tep:
    print("Nội dung từng dòng:")
    for dong in tep:
        print(dong.strip())
