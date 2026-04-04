# Bài 8: Lấy ra số lớn nhất trong list

_list = [11, 2, 23, 45, 6, 9]
_so_lon_nhat = _list[0]
for so in _list:
    if so > _so_lon_nhat:
        _so_lon_nhat = so

print('List:', _list)
print('Số lớn nhất:', _so_lon_nhat)
