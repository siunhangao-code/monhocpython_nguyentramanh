import tkinter as tk 

def xu_ly_submit(): 
    ho_ten = entry_ho_ten.get() 
    tuoi = entry_tuoi.get() 
    email = entry_email.get() 
    nhan_ket_qua.config(
        text=f"Da nhan: {ho_ten} - {tuoi} tuoi - {email}"
    ) 

def xu_ly_xoa():
    # Xóa trắng từ vị trí 0 đến cuối
    entry_ho_ten.delete(0, tk.END)
    entry_tuoi.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    nhan_ket_qua.config(text="")

cua_so = tk.Tk() 
cua_so.title("Form nhap thong tin") 
cua_so.geometry("400x280") 
cua_so.resizable(False, False) 

# Hàng 0: Họ tên
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w") 
entry_ho_ten = tk.Entry(cua_so, width=25) 
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10) 

# Hàng 1: Tuổi
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w") 
entry_tuoi = tk.Entry(cua_so, width=25) 
entry_tuoi.grid(row=1, column=1, padx=10, pady=10) 

# Hàng 2: Email
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w") 
entry_email = tk.Entry(cua_so, width=25) 
entry_email.grid(row=2, column=1, padx=10, pady=10) 

# Hàng 3: Các nút chức năng sử dụng chung 1 frame cho đẹp mắt
frame_nut = tk.Frame(cua_so)
frame_nut.grid(row=3, column=0, columnspan=2, pady=15)

nut_submit = tk.Button(frame_nut, text="Submit", command=xu_ly_submit, width=10) 
nut_submit.pack(side="left", padx=10)

nut_xoa = tk.Button(frame_nut, text="Xóa", command=xu_ly_xoa, width=10)
nut_xoa.pack(side="right", padx=10)

# Hàng 4: Nhãn kết quả
nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 11), fg="blue") 
nhan_ket_qua.grid(row=4, column=0, columnspan=2, pady=10) 

cua_so.mainloop()