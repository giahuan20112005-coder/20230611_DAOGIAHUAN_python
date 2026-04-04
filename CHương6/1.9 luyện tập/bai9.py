# Bài 9: Lấy ra số nhỏ nhất trong list

_list = [11, 2, 23, 45, 6, 9]
_so_nho_nhat = _list[0]
for so in _list:
    if so < _so_nho_nhat:
        _so_nho_nhat = so

print('List:', _list)
print('Số nhỏ nhất:', _so_nho_nhat)
