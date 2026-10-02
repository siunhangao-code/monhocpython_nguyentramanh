#hoat_dong_2.py

while True:
    try:
        so_luong = int(input("Nhap so luong (so nguyen duong): "))
        if so_luong > 0:
            break  # Thoát vòng lặp nếu nhập đúng số dương
        
        # Nếu nhập số <= 0, in ra thông báo và lặp lại
        print("So luong phai lon hon 0, vui long nhap lai.")
        
    except ValueError:
        # Bắt lỗi nếu người dùng nhập chữ hoặc ký tự không phải số nguyên
        print("Du lieu khong hop le, vui long nhap lai mot so nguyen.")

print("So luong hop le da nhap:", so_luong)