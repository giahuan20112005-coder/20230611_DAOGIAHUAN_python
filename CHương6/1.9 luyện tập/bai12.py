# Bài 12: Đếm số chuỗi thỏa điều kiện:
# - Độ dài chuỗi >= giá trị đầu vào
# - Kỳ tự đầu tiên và cuối cùng giống nhau

_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'iiz', '5yhy5']
_do_dai = int(input('Nhập vào độ dài chuỗi tối thiểu: '))

_so_luong = 0
for chuoi in _list:
    if len(chuoi) >= _do_dai and chuoi[0] == chuoi[-1]:
        _so_luong += 1

print('List ban đầu:', _list)
print('Độ dài tối thiểu:', _do_dai)
print('Số chuỗi thỏa điều kiện:', _so_luong)
