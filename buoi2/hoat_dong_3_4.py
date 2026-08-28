#Bài tập 3.1 – Các kiểu số
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j

print(type(so_nguyen))
print(type(so_thuc))
print(type(so_phuc))

print(float(so_nguyen))
print(int(so_thuc))
#Bài tập 3.2 – Hàm xử lý số
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a))
print(round(b))
print(round(b, 2))
print(pow(c, 2))
print(divmod(c, d))
#Bài tập 3.3 – Phương trình bậc hai
import math

a, b, c = 1, -3, 2

delta = b ** 2 - 4 * a * c

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
#Bài tập 4.1 – Indexing và slicing
cau = "Lap trinh Python rat thu vi"

print(cau[0])
print(cau[-1])
print(cau[4:10])
print(cau[:8])
print(cau[11:])
print(cau[::-1])

print(cau == cau[::-1])

#Bài tập 4.2 – String immutable
ten = "Nam"

# ten[0] = "T"
# Câu lệnh trên gây lỗi TypeError vì String là immutable.

ten_moi = "T" + ten[1:]

print(ten_moi)
#Bài tập 4.3 – Các phương thức String
cau = " Toi dang HOC Python rat vui "

print(cau.strip())
print(cau.strip().upper())
print(cau.strip().lower())
print(cau.strip().replace("HOC", "hoc"))
print(cau.strip().split())
print(len(cau.strip().split()))
print(cau.count("o"))
print(cau.find("Python"))
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))

#Bài tập 4.4 – Chuẩn hóa họ tên
ho_ten_tho = " nguyen tram anh "

ho_ten_sach = " ".join(ho_ten_tho.split()).title()

print(ho_ten_sach)
