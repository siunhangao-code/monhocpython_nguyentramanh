# Bai 4.1 - Tuple

#toa_do = (3, 5)

#print(toa_do)
#print(type(toa_do))

# Bai 4.2 - Unpacking tuple

#x, y = toa_do

#print("x =", x, "- y =", y)

#a, b = 10, 20

#a, b = b, a

#print("a =", a, "- b =", b)

# Bai 4.3 - Tra ve nhieu gia tri

c, d = 17, 5

thuong_du = divmod(c, d)

thuong, du = thuong_du

print(f"{c} chia {d} duoc thuong {thuong}, du {du}")
# Hoat dong 5 - Tinh khoang cach

import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt(
    (xb - xa) ** 2 + (yb - ya) ** 2
)

print(
    f"Khoang cach giua {diem_a} va {diem_b} la: "
    f"{round(khoang_cach, 2)}"
)
cac_diem = [(0, 0), (3, 4), (6, 8)]

goc = (0, 0)

for diem in cac_diem:
    x, y = diem

    khoang_cach = math.sqrt(
        (x - goc[0]) ** 2 + (y - goc[1]) ** 2
    )

    print(f"Diem {diem} cach goc toa do: {round(khoang_cach, 2)}")