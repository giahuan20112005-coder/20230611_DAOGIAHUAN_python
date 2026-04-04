# Bài 3: Loại bỏ trùng lặp trong một tuple để tạo tuple mới
# Ví dụ: _tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
# Kết quả mong muốn: _new_tuple = ('ab', 'b', 'e', 'c', 'd')

_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

# Ta chỉ giữ lần xuất hiện đầu tiên của mỗi giá trị.
seen = set()
new_list = []
for item in _tuple:
    if item not in seen:
        seen.add(item)
        new_list.append(item)

new_tuple = tuple(new_list)

print("Tuple ban đầu:", _tuple)
print("Tuple sau khi loại bỏ trùng lặp:", new_tuple)
