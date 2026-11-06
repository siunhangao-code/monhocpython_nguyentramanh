import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db

DANH_SACH_DANH_MUC = ["An uong", "Di lai", "Mua sam", "Giai tri", "Hoa don", "Khac"]

class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Chi tieu ca nhan")
        self.geometry("560x480")
        self.resizable(False, False)
        
        # Tạo file DB và bảng nếu chưa tồn tại
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        # 1. Khung nhập liệu
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ten khoan chi:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="So tien (VND):").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_tien = tk.Entry(khung_nhap, width=30)
        self.o_nhap_tien.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Danh muc:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC, width=27, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them khoan chi", command=self.xu_ly_them).grid(row=3, column=0, columnspan=2, pady=10)

        # 2. Khung danh sách
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_chi_tieu = tk.Listbox(khung_danh_sach, width=75, height=14)
        self.listbox_chi_tieu.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_chi_tieu.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_chi_tieu.config(yscrollcommand=thanh_cuon.set)

        # 3. Khung nút thao tác
        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button(khung_nut_thao_tac, text="Xoa khoan chi", command=self.xu_ly_xoa).grid(row=0, column=0, padx=10)
        tk.Button(khung_nut_thao_tac, text="Thong ke theo danh muc", command=self.xu_ly_thong_ke).grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox_chi_tieu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_chi_tieu()
        for chi_tieu in self.danh_sach_hien_tai:
            id_chi_tieu, ten, tien, danh_muc = chi_tieu
            self.listbox_chi_tieu.insert(tk.END, f"{ten} | {tien:,.0f} VND - ({danh_muc})")

    def xu_ly_them(self):
        ten = self.o_nhap_ten.get().strip()
        tien_str = self.o_nhap_tien.get().strip()
        danh_muc = self.chon_danh_muc.get()

        if ten == "" or tien_str == "":
            messagebox.showerror("Loi", "Vui long nhap day du ten khoan chi va so tien.")
            return
        try:
            tien = float(tien_str)
        except ValueError:
            messagebox.showerror("Loi", "So tien phai la mot so hop le.")
            return

        db.them_chi_tieu(ten, tien, danh_muc)
        self.o_nhap_ten.delete(0, tk.END)
        self.o_nhap_tien.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", f"Da them: {ten}")

    def xu_ly_xoa(self):
        lua_chon = self.listbox_chi_tieu.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot khoan chi de xoa.")
            return
        id_chi_tieu = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_chi_tieu(id_chi_tieu)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_danh_muc()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thong bao", "Chua co du lieu chi tieu de thong ke.")
            return

        cac_danh_muc = [dong[0] for dong in du_lieu_thong_ke]
        tong_tien = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(7, 5))
        plt.bar(cac_danh_muc, tong_tien, color="lightcoral")
        plt.title("Tong chi tieu theo danh muc")
        plt.xlabel("Danh muc")
        plt.ylabel("Tong tien (VND)")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    ung_dung = UngDungChiTieu()
    ung_dung.mainloop()