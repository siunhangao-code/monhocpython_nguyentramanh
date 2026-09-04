# Bai 1.1 - Khai bao va truy cap List
print("Bai 1.1 - Khai bao va truy cap List")
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
print(diem_so[0])
print(diem_so[-1])
print(diem_so[1:4])
print(diem_so[::2])
print(diem_so[::-1])
print()

# Bai 1.2 - Cac phuong thuc List
print("Bai 1.2 - Cac phuong thuc List")
ten_sv = ["An", "Binh", "Chi"]
ten_sv.append("Dung")
ten_sv.insert(1, "Em")
print(ten_sv)

ten_sv.remove("Chi")
pop_ra = ten_sv.pop()
print(ten_sv, "- da xoa:", pop_ra)

ten_sv.reverse()
print(ten_sv)

ten_sv.extend(["Giang", "Hoa"])
print(ten_sv)
print()

# Bai 2.1 - Duyet List bang for
print("Bai 2.1 - Duyet List bang for")
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0
for diem in diem_so:
    print(diem)
    tong += diem
print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))
print()

# Bai 2.2 - List long nhau
print("Bai 2.2 - List long nhau")
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In ra tung hang
for hang in ma_tran:
    print(hang)

# In ra tung phan tu
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()

tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran += phan_tu

print("Tong ma tran:", tong_ma_tran)
print()

# Bai 3.1 - Loc so chan le
print("Bai 3.1 - Loc so chan le")
day_so = list(range(1, 21))
so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]
print("So chan:", so_chan)
print("So le:", so_le)
print()

# Bai 3.2 - Bien doi phan tu
print("Bai 3.2 - Bien doi phan tu")
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]
print(diem_cong)