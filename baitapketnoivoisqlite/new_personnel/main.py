import sys
import os
from PyQt6 import uic, QtWidgets

from database import (
    add_person,
    delete_person,
    get_all_persons,
    initialize_database,
    search_persons,
    update_person,
)


class PersonnelWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "personnel.ui")
        uic.loadUi(ui_path, self)
        initialize_database()
        self.setup_table()
        self.connect_signals()
        self.refresh_table()

    def setup_table(self):
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["CCCD", "Họ và tên", "Ngày sinh", "Giới tính", "Địa chỉ"])

    def connect_signals(self):
        self.pushButtonAdd.clicked.connect(self.add_record)
        self.pushButtonUpdate.clicked.connect(self.update_record)
        self.pushButtonDelete.clicked.connect(self.delete_record)
        self.pushButtonClear.clicked.connect(self.clear_form)
        self.pushButtonSearch.clicked.connect(self.search_records)
        self.pushButtonRefresh.clicked.connect(self.refresh_table)
        self.tableWidget.itemSelectionChanged.connect(self.on_table_select)

    def get_form_data(self):
        return {
            "cccd": self.lineEditCCCD.text().strip(),
            "full_name": self.lineEditFullName.text().strip(),
            "birth_date": self.lineEditBirthDate.text().strip(),
            "gender": self.comboBoxGender.currentText().strip(),
            "address": self.plainTextEditAddress.toPlainText().strip(),
        }

    def clear_form(self):
        self.lineEditCCCD.setReadOnly(False)
        self.lineEditCCCD.clear()
        self.lineEditFullName.clear()
        self.lineEditBirthDate.clear()
        self.comboBoxGender.setCurrentIndex(0)
        self.plainTextEditAddress.clear()
        self.tableWidget.clearSelection()

    def validate_form(self, data):
        if not data["cccd"]:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập số CCCD.")
            return False
        if not data["full_name"]:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập họ và tên.")
            return False
        return True

    def add_record(self):
        data = self.get_form_data()
        if not self.validate_form(data):
            return
        try:
            add_person(data["cccd"], data["full_name"], data["birth_date"], data["gender"], data["address"])
            QtWidgets.QMessageBox.information(self, "Thành công", "Đã thêm nhân sự mới.")
            self.refresh_table()
            self.clear_form()
        except Exception as error:
            QtWidgets.QMessageBox.critical(self, "Lỗi", str(error))

    def update_record(self):
        data = self.get_form_data()
        if not self.validate_form(data):
            return
        try:
            update_person(data["cccd"], data["full_name"], data["birth_date"], data["gender"], data["address"])
            QtWidgets.QMessageBox.information(self, "Thành công", "Đã cập nhật nhân sự.")
            self.refresh_table()
            self.clear_form()
        except Exception as error:
            QtWidgets.QMessageBox.critical(self, "Lỗi", str(error))

    def delete_record(self):
        cccd = self.lineEditCCCD.text().strip()
        if not cccd:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn hoặc nhập CCCD để xóa.")
            return
        if QtWidgets.QMessageBox.question(
            self,
            "Xác nhận",
            f"Xóa nhân sự CCCD {cccd}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
        ) != QtWidgets.QMessageBox.StandardButton.Yes:
            return
        try:
            delete_person(cccd)
            QtWidgets.QMessageBox.information(self, "Thành công", "Đã xóa nhân sự.")
            self.refresh_table()
            self.clear_form()
        except Exception as error:
            QtWidgets.QMessageBox.critical(self, "Lỗi", str(error))

    def refresh_table(self):
        self.load_table(get_all_persons())

    def search_records(self):
        results = search_persons(
            cccd=self.lineEditSearchCCCD.text().strip(),
            full_name=self.lineEditSearchName.text().strip(),
            address=self.lineEditSearchAddress.text().strip(),
        )
        self.load_table(results)

    def load_table(self, records):
        self.tableWidget.setRowCount(0)
        for record in records:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, value in enumerate(record):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))

    def on_table_select(self):
        items = self.tableWidget.selectedItems()
        if not items:
            return
        self.lineEditCCCD.setText(items[0].text())
        self.lineEditCCCD.setReadOnly(True)
        self.lineEditFullName.setText(items[1].text())
        self.lineEditBirthDate.setText(items[2].text())
        self.comboBoxGender.setCurrentText(items[3].text())
        self.plainTextEditAddress.setPlainText(items[4].text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PersonnelWindow()
    window.show()
    sys.exit(app.exec())
