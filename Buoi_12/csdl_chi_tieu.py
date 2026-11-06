import sqlite3

TEN_FILE_CSDL = "chi_tieu.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute('''
        CREATE TABLE IF NOT EXISTS chi_tieu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_khoan_chi TEXT NOT NULL,
            so_tien REAL NOT NULL,
            danh_muc TEXT NOT NULL
        )
    ''')
    ket_noi.commit()
    ket_noi.close()

def them_chi_tieu(ten_khoan_chi, so_tien, danh_muc):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO chi_tieu (ten_khoan_chi, so_tien, danh_muc) VALUES (?, ?, ?)",
        (ten_khoan_chi, so_tien, danh_muc)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_chi_tieu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_khoan_chi, so_tien, danh_muc FROM chi_tieu ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_chi_tieu(id_chi_tieu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM chi_tieu WHERE id = ?", (id_chi_tieu,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_danh_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT danh_muc, SUM(so_tien) FROM chi_tieu GROUP BY danh_muc")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua