# Mini project - Dang ky thong tin ca nhan

ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")

# Chuan hoa ho ten
ho_ten_chuan = " ".join(ho_ten.split()).title()

# Kiem tra so dien thoai
sdt_hop_le = len(sdt) == 10

# Kiem tra email
email_hop_le = "@" in email

# Hien thi ket qua
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")