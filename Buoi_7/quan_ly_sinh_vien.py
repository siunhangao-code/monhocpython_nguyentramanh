# QUẢN LÝ SINH VIÊN - ĐỒ ÁN BUỔI 7
# Sử dụng: List, Dictionary, Vòng lặp, Hàm, và Try-Except

# 1. Khai báo dữ liệu ban đầu (List chứa Dictionary)
danh_sach_sv = [
    {"ma_sv": "SV01", "ten": "Nguyen Van A", "diem": 8.5, "hoc_luc": "Gioi"},
    {"ma_sv": "SV02", "ten": "Tran Thi B", "diem": 6.5, "hoc_luc": "Kha"}
]

# 2. Hàm hỗ trợ: Nhập số điểm an toàn bằng try-except
def nhap_diem_an_toan(loi_nhac):
    while True:
        try:
            # Ép kiểu float vì điểm có thể là số thập phân
            diem = float(input(loi_nhac))
            if 0 <= diem <= 10:
                return diem
            else:
                print("-> Điểm phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
        except ValueError:
            # Bắt lỗi nếu người dùng nhập chữ cái thay vì số
            print("-> Dữ liệu không hợp lệ, vui lòng nhập một số.")

# 3. Hàm hỗ trợ: Xếp loại học lực
def xep_loai_hoc_luc(diem):
    if diem >= 8.0:
        return "Gioi"
    elif diem >= 6.5:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

# 4. Hàm hiển thị danh sách
def hien_thi_danh_sach():
    if len(danh_sach_sv) == 0:
        print("-> Danh sách sinh viên trống.")
        return
    
    print("\n" + "=" * 55)
    # Dùng f-string định dạng khoảng cách giống bài khách sạn
    print(f"{'Ma SV': <10}{'Ho va Ten': <20}{'Diem': <10}{'Hoc Luc': <15}")
    print("-" * 55)
    for sv in danh_sach_sv:
        print(f"{sv['ma_sv']: <10}{sv['ten']: <20}{sv['diem']: <10.2f}{sv['hoc_luc']: <15}")
    print("=" * 55)

# 5. Hàm thêm sinh viên
def them_sinh_vien():
    print("\n--- THÊM SINH VIÊN MỚI ---")
    ma_sv = input("Nhap ma sinh vien: ").strip().upper()
    
    # Kiểm tra trùng mã SV
    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            print(f"-> Mã sinh viên {ma_sv} đã tồn tại!")
            return
            
    ten = input("Nhap ten sinh vien: ").strip().title()
    diem = nhap_diem_an_toan("Nhap diem trung binh (0-10): ")
    hoc_luc = xep_loai_hoc_luc(diem)
    
    # Thêm dict mới vào list
    danh_sach_sv.append({
        "ma_sv": ma_sv,
        "ten": ten,
        "diem": diem,
        "hoc_luc": hoc_luc
    })
    print(f"-> Đã thêm sinh viên {ten} thành công!")

# 6. Hàm xóa sinh viên
def xoa_sinh_vien():
    print("\n--- XÓA SINH VIÊN ---")
    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()
    
    for i in range(len(danh_sach_sv)):
        if danh_sach_sv[i]["ma_sv"] == ma_sv:
            ten_xoa = danh_sach_sv[i]["ten"]
            danh_sach_sv.pop(i) # Xóa phần tử tại vị trí i
            print(f"-> Đã xóa sinh viên {ten_xoa} thành công.")
            return
            
    print(f"-> Không tìm thấy sinh viên có mã {ma_sv}.")

# 7. Menu chính
def chay_chuong_trinh():
    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Hien thi danh sach sinh vien")
        print("2. Them sinh vien moi")
        print("3. Xoa sinh vien")
        print("0. Thoat chuong trinh")
        
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        
        if lua_chon == "1":
            hien_thi_danh_sach()
        elif lua_chon == "2":
            them_sinh_vien()
        elif lua_chon == "3":
            xoa_sinh_vien()
        elif lua_chon == "0":
            print("Cam on em da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

# Khởi chạy chương trình
if __name__ == "__main__":
    chay_chuong_trinh()