import tkinter as tk
import random
from tkinter import messagebox

# Hàm xử lý khi bấm nút "Có"
def chon_co():
    # Hiển thị một hộp thoại thông báo (MessageBox)
    messagebox.showinfo("Kết quả", "Mình biết mà! Trâm Anh cũng rất yêu bạn <3")
    nhan_ket_qua.config(text="Quá tuyệt vời! Chúc hai bạn hạnh phúc!", fg="green")

# Hàm làm cho nút "Không" chạy trốn khi chuột chạm vào
def chay_tron(event):
    # Lấy kích thước hiện tại của cửa sổ
    max_x = cua_so.winfo_width() - 80  # Trừ đi chiều rộng của nút
    max_y = cua_so.winfo_height() - 40 # Trừ đi chiều cao của nút
    
    # Nếu cửa sổ chưa hiển thị (lúc mới mở), gán giá trị mặc định
    if max_x <= 0 or max_y <= 0:
        max_x = 420
        max_y = 360

    # Tạo tọa độ x, y ngẫu nhiên mới
    toa_do_x = random.randint(10, max_x)
    toa_do_y = random.randint(10, max_y)
    
    # Dùng place() để di chuyển nút "Không" đến tọa độ mới
    nut_khong.place(x=toa_do_x, y=toa_do_y)
    nhan_ket_qua.config(text="Ê ê, đố bạn bấm được nút 'Không' đấy =)))", fg="red")

# Khởi tạo cửa sổ
cua_so = tk.Tk()
cua_so.title("Câu hỏi hệ trọng")
cua_so.geometry("500x400") # Làm cửa sổ to hơn một chút để nút có chỗ chạy
cua_so.resizable(False, False)

# Nhãn hiển thị câu hỏi
nhan_cau_hoi = tk.Label(cua_so, text="Bạn có yêu Trâm Anh không?", font=("Arial", 18, "bold"))
nhan_cau_hoi.pack(pady=40)

# Nhãn để hiển thị trạng thái trêu đùa
nhan_ket_qua = tk.Label(cua_so, text="Hãy lựa chọn đi nào!", font=("Arial", 12, "italic"))
nhan_ket_qua.pack(pady=10)

# Nút "Có" - Dùng place để cố định vị trí
nut_co = tk.Button(cua_so, text="Có", font=("Arial", 14, "bold"), width=10, bg="lightgreen", command=chon_co)
nut_co.place(x=100, y=180)

# Nút "Không" - Dùng place để cố định vị trí ban đầu
nut_khong = tk.Button(cua_so, text="Không", font=("Arial", 14, "bold"), width=10, bg="lightcoral")
nut_khong.place(x=270, y=180)

# BẮT SỰ KIỆN: Bất cứ khi nào con trỏ chuột chạm vào (<Enter>) nút "Không", hàm chay_tron sẽ được gọi
nut_khong.bind("<Enter>", chay_tron)

# Cập nhật giao diện trước khi lấy kích thước
cua_so.update()

# Chạy vòng lặp
cua_so.mainloop()