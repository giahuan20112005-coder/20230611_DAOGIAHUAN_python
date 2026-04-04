# Bài 3: Cho đầu vào là _list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Viết chương trình tạo 2 list mới: một list chỉ chứa số chẵn, một list chỉ chứa số lẻ.

_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_list_chan = []
_list_le = []

for so in _list:
    if so % 2 == 0:
        _list_chan.append(so)
    else:
        _list_le.append(so)

print('List ban đầu:', _list)
print('List số chẵn:', _list_chan)
print('List số lẻ:', _list_le)
