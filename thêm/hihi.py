import tkinter as tk
import random
from tkinter import messagebox

# Biến toàn cục đếm số lần cố gắng bấm nút "Không"
so_lan_ne = 0

# Danh sách các câu trêu đùa tăng dần độ "nhây"
cau_treu_dua = [
    "Ê ê, đố bấm được nút 'Không' đấy =)))",
    "Còn lâu mới chạm được nha!",
    "Mỏi tay chưa? Bỏ cuộc đi!",
    "Bấm 'Có' cho nhanh đi bạn êii",
    "Nút 'Không' sắp chạy ra ngoài vũ trụ rồi!",
    "Ngoan ngoãn chấp nhận sự thật đi <3",
    "Trâm Anh là chân ái, đừng cố cãi!"
]

def chon_co():
    # Xóa các nút hiện tại trên màn hình
    nut_co.destroy()
    nut_khong.destroy()
    
    # Đổi giao diện sang chế độ "Chúc mừng"
    cua_so.config(bg="#ffe4e1") # Đổi nền sang màu hồng nhạt
    nhan_cau_hoi.config(text="Mình biết mà! Trâm Anh cũng yêu bạn <3", 
                        fg="#ff1493", bg="#ffe4e1", font=("Arial", 22, "bold"))
    nhan_ket_qua.config(text="Mãi yêuuuuu! 💖💖💖", 
                        fg="#ff69b4", bg="#ffe4e1", font=("Arial", 16, "italic"))
    
    # Kích hoạt hiệu ứng mưa trái tim
    tao_trai_tim()

def tao_trai_tim():
    # Tạo ra các nhãn chứa biểu tượng trái tim với kích cỡ ngẫu nhiên
    tim = tk.Label(cua_so, text="❤️", font=("Arial", random.randint(15, 40)), bg="#ffe4e1", fg="red")
    tim.place(x=random.randint(10, 550), y=random.randint(10, 450))
    
    # Đặt thời gian lặp lại để tạo trái tim mới liên tục sau mỗi 150 milliseconds
    cua_so.after(150, tao_trai_tim)

def chay_tron(event):
    global so_lan_ne
    so_lan_ne += 1

    # 1. Thay đổi câu trêu đùa (cứ mỗi 2 lần lách chuột sẽ đổi 1 câu)
    index_cau = min(so_lan_ne // 2, len(cau_treu_dua) - 1)
    nhan_ket_qua.config(text=cau_treu_dua[index_cau], fg="red")

    # 2. Làm nút "Có" to dần lên để ép người dùng bấm
    kich_thuoc_font_co = min(14 + so_lan_ne * 4, 60) # Tối đa font size là 60
    nut_co.config(font=("Arial", kich_thuoc_font_co, "bold"))

    # 3. Tính toán vị trí ngẫu nhiên mới cho nút "Không"
    max_x = cua_so.winfo_width() - nut_khong.winfo_width()
    max_y = cua_so.winfo_height() - nut_khong.winfo_height()
    
    if max_x <= 0 or max_y <= 0:
        max_x = 450
        max_y = 350

    toa_do_x = random.randint(10, max_x)
    toa_do_y = random.randint(100, max_y) # Né phần tiêu đề ở trên cùng (y > 100)
    
    # Chuyển anchor về NW (chuẩn) để nút nhảy chính xác theo tọa độ tuyệt đối
    nut_khong.place(x=toa_do_x, y=toa_do_y, anchor=tk.NW)

# ================= CẤU HÌNH GIAO DIỆN CHÍNH =================

cua_so = tk.Tk()
cua_so.title("Câu hỏi hệ trọng nhất thế kỷ")
cua_so.geometry("600x500") 
cua_so.resizable(False, False)
cua_so.config(bg="#f0f8ff") # Nền màu xanh lơ nhạt dễ thương

# Nhãn hiển thị câu hỏi
nhan_cau_hoi = tk.Label(cua_so, text="Bạn có yêu Trâm Anh không?", 
                        font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#333333")
nhan_cau_hoi.pack(pady=40)

# Nhãn trạng thái
nhan_ket_qua = tk.Label(cua_so, text="Hãy suy nghĩ kỹ và lựa chọn đi nào!", 
                        font=("Arial", 12, "italic"), bg="#f0f8ff", fg="#555555")
nhan_ket_qua.pack(pady=10)

# Nút "Có" - Dùng relx/rely với anchor CENTER để khi phình to nó vẫn nằm giữa trục của nó
nut_co = tk.Button(cua_so, text="Có", font=("Arial", 14, "bold"), width=8, 
                   bg="#90ee90", activebackground="#32cd32", command=chon_co)
nut_co.place(relx=0.35, rely=0.6, anchor=tk.CENTER)

# Nút "Không" - Vị trí khởi tạo
nut_khong = tk.Button(cua_so, text="Không", font=("Arial", 14, "bold"), width=8, 
                      bg="#ffb6c1", activebackground="#ff69b4")
nut_khong.place(relx=0.65, rely=0.6, anchor=tk.CENTER)

# Ràng buộc sự kiện chạm chuột cho nút "Không"
nut_khong.bind("<Enter>", chay_tron)

# Cập nhật GUI trước khi tính toán kích thước
cua_so.update()

# Chạy ứng dụng
cua_so.mainloop()