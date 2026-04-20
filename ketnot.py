import sqlite3

# Kết nối đến database (tạo file demo.db nếu chưa có)
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# --- CÂU A: Lấy danh sách nhân viên là MANAGER ---
def get_managers():
    print("--- Danh sách MANAGER ---")
    query = "SELECT * FROM employee WHERE job = 'MANAGER'"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

# --- CÂU B: Insert thông tin phòng làm việc thực tế ---
def insert_department():
    # Giả sử: ID: 50, Tên: IT, Địa điểm: Hà Nội
    query = "INSERT INTO department (dept_id, dept_name, location) VALUES (?, ?, ?)"
    values = (50, 'IT Department', 'Ha Noi')
    cursor.execute(query, values)
    conn.commit()
    print("Đã thêm phòng làm việc mới.")

# --- CÂU C: Insert thông tin thực tế của bản thân ---
def insert_myself():
    # Giả sử: ID: 999, Tên: Nguyen Van A, Job: DEVELOPER, Dept: 50
    query = "INSERT INTO employee (id, name, job, dept_id) VALUES (?, ?, ?, ?)"
    values = (999, 'Nguyen Van A', 'DEVELOPER', 50)
    cursor.execute(query, values)
    conn.commit()
    print("Đã thêm thông tin bản thân.")

# --- CÂU D: Cập nhật thông tin nhân viên tên CLARK thành thông tin của bạn ---
def update_clark():
    query = "UPDATE employee SET name = ?, job = ? WHERE name = 'CLARK'"
    values = ('Nguyen Van A', 'SENIOR DEV')
    cursor.execute(query, values)
    conn.commit()
    print("Đã cập nhật thông tin của CLARK.")

# --- CÂU E: Xóa thông tin nhân viên tên MILLER ---
def delete_miller():
    query = "DELETE FROM employee WHERE name = 'MILLER'"
    cursor.execute(query)
    conn.commit()
    print("Đã xóa nhân viên MILLER.")

# --- THỰC THI ---
# Lưu ý: Các hàm insert/update/delete cần bảng đã tồn tại để không báo lỗi
# get_managers()
# insert_department()
# ...