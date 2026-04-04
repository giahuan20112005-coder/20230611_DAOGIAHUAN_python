# Bài 2: Loại bỏ các phần tử có giá trị giống nhau trong tuple để tạo tuple mới
# Ví dụ: _tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
# Kết quả mong muốn: _new_tuple = ('b', 'c', 'd')

_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

# Ta giữ lại các phần tử chỉ xuất hiện đúng một lần trong tuple ban đầu.
new_tuple = tuple(item for item in _tuple if _tuple.count(item) == 1)

print("Tuple ban đầu:", _tuple)
print("Tuple mới chỉ giữ phần tử không trùng lặp:", new_tuple)
