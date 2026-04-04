# Bài 1: Thêm phần tử 'c' vào vị trí số 2 trong tuple ban đầu
# _tuple = ('a', 'b', 'd', 'e')
# Kết quả mong muốn: _new_tuple = ('a', 'b', 'c', 'd', 'e')

_tuple = ('a', 'b', 'd', 'e')

# Vì tuple không thể thay đổi trực tiếp, ta tạo tuple mới bằng cách ghép 3 phần:
# phần trước vị trí chèn, phần chèn, phần sau vị trí chèn.
new_tuple = _tuple[:2] + ('c',) + _tuple[2:]

print("Tuple ban đầu:", _tuple)
print("Tuple sau khi chèn 'c' vào vị trí 2:", new_tuple)
