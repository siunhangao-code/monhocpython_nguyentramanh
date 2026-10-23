import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("May Tinh Bo Tui - PyQt5")
        self.resize(300, 400)
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        layout_chinh = QVBoxLayout()
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setAlignment(Qt.AlignRight) # Căn phải giống máy tính thật
        self.man_hinh.setStyleSheet("font-size: 30px; padding: 10px;")
        layout_chinh.addWidget(self.man_hinh)
        layout_phim = QGridLayout()
        danh_sach_phim = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for hang, ds_cot in enumerate(danh_sach_phim):
            for cot, ky_tu in enumerate(ds_cot):
                nut = QPushButton(ky_tu)
                nut.setStyleSheet("font-size: 20px; padding: 15px;")
                # Dùng lambda để gửi chính xác ký tự của nút đó vào hàm xử lý
                nut.clicked.connect(lambda ch, kt=ky_tu: self.xu_ly_bam_nut(kt))
                layout_phim.addWidget(nut, hang, cot)
                
        layout_chinh.addLayout(layout_phim)
        self.setLayout(layout_chinh)

    def xu_ly_bam_nut(self, ky_tu):
        if ky_tu == 'C':
            self.man_hinh.clear()
        elif ky_tu == '=':
            bieu_thuc = self.man_hinh.text()
            try:

                ket_qua = str(eval(bieu_thuc))
                self.man_hinh.setText(ket_qua)
            except Exception:
                self.man_hinh.setText("Lỗi")
        else:
            noi_dung_hien_tai = self.man_hinh.text()
            if noi_dung_hien_tai == "Lỗi":
                noi_dung_hien_tai = ""
            self.man_hinh.setText(noi_dung_hien_tai + ky_tu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())