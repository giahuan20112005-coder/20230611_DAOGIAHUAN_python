class HocVien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    def hien_thi_thong_tin(self):
        print('--- Thông tin học viên ---')
        print(f'Họ tên   : {self.ho_ten}')
        print(f'Ngày sinh: {self.ngay_sinh}')
        print(f'Email    : {self.email}')
        print(f'Điện thoại: {self.dien_thoai}')
        print(f'Địa chỉ  : {self.dia_chi}')
        print(f'Lớp      : {self.lop}')
        print('-------------------------')

    def doi_thong_tin(self, dia_chi='Hà Nội', lop='IT12.x'):
        self.dia_chi = dia_chi
        self.lop = lop
        print('Đã đổi địa chỉ và lớp thành công.')


def main():
    hoc_vien = HocVien(
        ho_ten='Nguyễn Văn A',
        ngay_sinh='01/01/2000',
        email='nguyenvana@example.com',
        dien_thoai='0123456789',
        dia_chi='TP. Hồ Chí Minh',
        lop='CNTT1'
    )

    hoc_vien.hien_thi_thong_tin()

    print('\nThay đổi thông tin với tham số mặc định:')
    hoc_vien.doi_thong_tin()
    hoc_vien.hien_thi_thong_tin()

    print('\nThay đổi thông tin với tham số mới:')
    hoc_vien.doi_thong_tin(dia_chi='Đà Nẵng', lop='IT20')
    hoc_vien.hien_thi_thong_tin()


if __name__ == '__main__':
    main()
