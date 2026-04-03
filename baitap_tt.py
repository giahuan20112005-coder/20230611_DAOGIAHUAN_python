# Bài tập luyện tập - Code thuần Việt
# Tác giả: [Tên của bạn]

# 1. Hàm tính tổng 2 số truyền vào
def tinh_tong_2_so(a, b):
    return a + b

# 2. Hàm tính tổng các số truyền vào (danh sách)
def tinh_tong_cac_so(danh_sach):
    return sum(danh_sach)

# 3. Hàm kiểm tra một số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Tìm các số nguyên tố trong khoảng [a, b]
def cac_so_nguyen_to_trong_khoang(a, b):
    return [i for i in range(a, b + 1) if la_so_nguyen_to(i)]

# 5. Hàm kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    if n < 2:
        return False
    tong = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            tong += i
    return tong == n

# 6. Tìm các số hoàn hảo trong khoảng [a, b]
def cac_so_hoan_hao_trong_khoang(a, b):
    return [i for i in range(a, b + 1) if la_so_hoan_hao(i)]

# 7. Menu chọn thực thi các hàm trên
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng các số trong danh sách")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm các số nguyên tố trong khoảng [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm các số hoàn hảo trong khoảng [a, b]")
        print("0. Thoát")
        lua_chon = input("Nhập lựa chọn: ")
        if lua_chon == '1':
            a = int(input("Nhập số thứ nhất: "))
            b = int(input("Nhập số thứ hai: "))
            print("Tổng là:", tinh_tong_2_so(a, b))
        elif lua_chon == '2':
            ds = input("Nhập các số, cách nhau bởi dấu cách: ")
            danh_sach = list(map(int, ds.split()))
            print("Tổng là:", tinh_tong_cac_so(danh_sach))
        elif lua_chon == '3':
            n = int(input("Nhập số cần kiểm tra: "))
            if la_so_nguyen_to(n):
                print(n, "là số nguyên tố")
            else:
                print(n, "không phải là số nguyên tố")
        elif lua_chon == '4':
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số nguyên tố:", cac_so_nguyen_to_trong_khoang(a, b))
        elif lua_chon == '5':
            n = int(input("Nhập số cần kiểm tra: "))
            if la_so_hoan_hao(n):
                print(n, "là số hoàn hảo")
            else:
                print(n, "không phải là số hoàn hảo")
        elif lua_chon == '6':
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số hoàn hảo:", cac_so_hoan_hao_trong_khoang(a, b))
        elif lua_chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại!")

if __name__ == "__main__":
    menu()