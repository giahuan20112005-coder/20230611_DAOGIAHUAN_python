# Bài 11: Nhập vào từ bàn phím số n và list cho trước, tìm các từ có độ dài lớn hơn n từ list đó.

_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'iiz', '5yhy5']
n = int(input('Nhập vào số n: '))

_ket_qua = []
for tu in _list:
    if len(tu) > n:
        _ket_qua.append(tu)

print('List ban đầu:', _list)
print('Số n:', n)
print('Các từ có độ dài > n:', _ket_qua)
