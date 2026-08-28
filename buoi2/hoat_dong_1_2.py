#Bài tập 1.1 – input() và ép kiểu
#ho_ten = input("Nhap ho ten: ")
#nam_sinh = int(input("Nhap nam sinh: "))
#diem_tb = float(input("Nhap diem trung binh: "))

#print(ho_ten)
#print(nam_sinh)
#print(diem_tb)
#Bài tập 1.2 – print() với sep và end
#print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
#print("Dong 1", end=" | ")
#print("Dong 2")
#Bài tập 1.3 – Ba cách định dạng chuỗi
#ho_ten = input("Nhap ho ten: ")
#nam_sinh = int(input("Nhap nam sinh: "))
#diem_tb = float(input("Nhap diem trung binh: "))

# f-string
#print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# str.format()
#print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(
#    ho_ten, nam_sinh, diem_tb
#))

# Toan tu %
#print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" %
#      (ho_ten, nam_sinh, diem_tb))

#Bài tập 2.1 – Chú thích
# Chu thich mot dong: khai bao thong tin sinh vien

"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""

#ho_ten_2 = "Nguyen Nhu Quynh"  # bien luu ho ten

#print(ho_ten_2)
#Bài tập 2.2 – Trích dẫn và escape
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"

s3 = '''Day la
mot chuoi
nhieu dong'''

s4 = "Duong dan: C:\\Python\\data"

s5 = r"Duong dan raw: C:\Python\data"

s6 = "Toi ten la \"Nam\", con ban ten gi?"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)