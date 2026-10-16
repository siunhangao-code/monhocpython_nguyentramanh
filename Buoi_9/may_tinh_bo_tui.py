import tkinter as tk

def nhap(gia_tri):
    bieu_thuc.set(bieu_thuc.get() + gia_tri)

def tinh():
    try:
        ket_qua = str(eval(bieu_thuc.get()))
        bieu_thuc.set(ket_qua)
    except:
        bieu_thuc.set("Loi")

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")

bieu_thuc = tk.StringVar()
tk.Entry(cua_so, textvariable=bieu_thuc, width=20, font=("Arial", 14)).grid(row=0, column=0, columnspan=4)

cac_nut = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

hang = 1
cot = 0
for nut in cac_nut:
    if nut == '=':
        tk.Button(cua_so, text=nut, width=5, command=tinh).grid(row=hang, column=cot)
    elif nut == 'C':
        tk.Button(cua_so, text=nut, width=5, command=lambda: bieu_thuc.set("")).grid(row=hang, column=cot)
    else:
        tk.Button(cua_so, text=nut, width=5, command=lambda n=nut: nhap(n)).grid(row=hang, column=cot)
    
    cot += 1
    if cot > 3:
        cot = 0
        hang += 1

cua_so.mainloop()