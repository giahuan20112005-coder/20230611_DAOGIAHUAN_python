# Bài 5: Cho danh sách đầu vào _list = ['zero', 'three']
# Tạo danh sách mới _new = ['zero', 'one', 'two', 'three'] bằng cách thêm các phần tử vào danh sách ban đầu.

_list = ['zero', 'three']
_new = _list.copy()
_new.insert(1, 'one')
_new.insert(2, 'two')

print('List ban đầu:', _list)
print('List mới:', _new)
