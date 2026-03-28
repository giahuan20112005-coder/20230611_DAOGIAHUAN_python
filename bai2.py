# Bài 2: Kiểm tra 3 cạnh có phải tam giác
print("Nhập vào 3 số nguyên dương là độ dài 3 cạnh:")
canh_a = int(input("Cạnh a = "))
canh_b = int(input("Cạnh b = "))
canh_c = int(input("Cạnh c = "))
if canh_a + canh_b > canh_c and canh_a + canh_c > canh_b and canh_b + canh_c > canh_a:
    print("Độ dài ba cạnh tam giác")
else:
    print("Đây không phải độ dài ba cạnh tam giác")
