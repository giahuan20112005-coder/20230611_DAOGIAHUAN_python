# Bài 7: Tạo một list mới bằng cách loại bỏ các phần tử trùng nhau từ list đầu vào

_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
_new = []
for phan_tu in _list:
    if phan_tu not in _new:
        _new.append(phan_tu)

print('List ban đầu:', _list)
print('List mới:', _new)
