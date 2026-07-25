"""
BÀI TẬP: VẼ CẢNH BIỂN CÓ THUYỀN ĐÁNH CÁ BẰNG TURTLE
Dành cho học sinh lớp 6 - Môn Tin học
------------------------------------------
Chương trình vẽ:
  1. Bầu trời (màu xanh da trời)
  2. Mặt biển (màu xanh dương)
  3. Mặt trời (hình tròn màu vàng)
  4. Vài gợn sóng nhẹ rải khắp mặt biển (số lượng, vị trí NGẪU NHIÊN)
  5. Ba chiếc thuyền đánh cá (to nhỏ khác nhau cho có xa - gần)
  6. Vài chú chim bay trên bầu trời (số lượng, vị trí NGẪU NHIÊN)
  7. Vài con cá bơi dưới biển (số lượng, vị trí, kích thước, màu NGẪU NHIÊN)

Mỗi lần chạy chương trình, do dùng random.randint(), số lượng và
vị trí của sóng/chim/cá sẽ khác nhau -> bức tranh không bao giờ giống hệt lần trước!
"""

import turtle
import random

# ===== BƯỚC 1: THIẾT LẬP MÀN HÌNH =====
man_hinh = turtle.Screen()
man_hinh.title("Buc tranh: Thuyen ngoai bien")
man_hinh.bgcolor("skyblue")
man_hinh.setup(width=700, height=550)

# Con rùa để vẽ
rua = turtle.Turtle()
rua.speed(0)          # tốc độ vẽ (1 chậm - 10 nhanh)
rua.width(2)


# ===== HÀM PHỤ: DI CHUYỂN BÚT MÀ KHÔNG VẼ =====
def nhac_but_toi(x, y):
    rua.penup()
    rua.goto(x, y)
    rua.pendown()


# ===== BƯỚC 2: VẼ MẶT BIỂN (HÌNH CHỮ NHẬT MÀU XANH) =====
def ve_bien():
    nhac_but_toi(-350, 0)
    rua.color("dodgerblue")
    rua.begin_fill()
    for canh in range(2):
        rua.forward(700)
        rua.right(90)
        rua.forward(275)
        rua.right(90)
    rua.end_fill()


# ===== BƯỚC 3: VẼ MẶT TRỜI (HÌNH TRÒN MÀU VÀNG) =====
def ve_mat_troi():
    nhac_but_toi(230, 150)
    rua.color("gold")
    rua.begin_fill()
    rua.circle(40)
    rua.end_fill()


# ===== BƯỚC 4: VẼ GỢN SÓNG (ĐƯỜNG LƯỢN NGANG) =====
def ve_song(x, y, so_luon=6, color = "white"):
    nhac_but_toi(x, y)
    rua.setheading(0)      # hướng ngang, đi sang phải
    rua.color(color)
    rua.pensize(2)
    for i in range(so_luon):
        ranNum = random.randint(8, 12)
        rua.left(30)
        rua.forward(ranNum)
        rua.right(60)
        rua.forward(ranNum)
        rua.left(30)        # quay lại đúng hướng ngang ban đầu
    rua.color("black")
    rua.pensize(2)


# ===== BƯỚC 5: VẼ 1 CHIẾC THUYỀN ĐÁNH CÁ =====
# x_offset: thuyền nằm ở vị trí nào trên trục ngang
# ty_le  : tỉ lệ phóng to/thu nhỏ (thuyền xa thì ty_le nhỏ hơn)

# Hàm phụ: phóng to/thu nhỏ 1 điểm theo ty_le, rồi dịch sang phải/trái theo x_offset
def phong_to_va_dich_diem(diem_goc, ty_le, x_offset):
    danh_sach_diem_moi = []            # tạo 1 danh sách rỗng để chứa kết quả
    for px, py in diem_goc:            # lấy lần lượt từng điểm (px, py) trong danh sách gốc
        x_moi = px * ty_le + x_offset  # phóng to/nhỏ theo trục x, rồi dịch sang trái/phải
        y_moi = py * ty_le             # phóng to/nhỏ theo trục y
        danh_sach_diem_moi.append((x_moi, y_moi))   # thêm điểm mới vào danh sách kết quả
    return danh_sach_diem_moi


def ve_thuyen(x_offset, ty_le=1.0):
    # ---- thân thuyền (hình thang màu nâu) ----
    diem_than_goc = [(-70, 0), (70, 0), (45, -55), (-45, -55)]
    diem_than = phong_to_va_dich_diem(diem_than_goc, ty_le, x_offset)
    x_bat_dau, y_bat_dau = diem_than[0]    # tách điểm đầu tiên ra thành 2 biến x, y
    nhac_but_toi(x_bat_dau, y_bat_dau)
    rua.color("saddlebrown")
    rua.begin_fill()
    for diem in diem_than:             # đi qua các điểm còn lại
        x_diem, y_diem = diem              # tách điểm đó ra thành x, y
        rua.goto(x_diem, y_diem)
    rua.goto(x_bat_dau, y_bat_dau)          # quay lại điểm đầu tiên để khép kín hình
    rua.end_fill()

    # ---- cột buồm (đường thẳng đứng) ----
    nhac_but_toi(x_offset, 0)
    rua.color("black")
    rua.goto(x_offset, 140 * ty_le)

    # ---- cánh buồm (hình tam giác màu trắng) ----
    diem_buom_goc = [(0, 135), (0, 40), (65, 65)]
    diem_buom = phong_to_va_dich_diem(diem_buom_goc, ty_le, x_offset)
    x_bat_dau, y_bat_dau = diem_buom[0] 
    nhac_but_toi(x_bat_dau, y_bat_dau)
    rua.fillcolor("white")
    rua.begin_fill()
    for p in diem_buom:
        x_diem, y_diem = p
        rua.goto(x_diem, y_diem )
    rua.goto(x_bat_dau, y_bat_dau)          # quay lại điểm đầu tiên để khép kín hình
    rua.end_fill()


# ===== BƯỚC 7: VẼ 1 CON CÁ BƠI DƯỚI BIỂN =====
# Thân cá là hình tròn, đuôi cá là hình tam giác nhỏ, thêm 1 chấm làm mắt
def ve_ca(x, y, kich_thuoc=15):
    # Chọn ngẫu nhiên 1 màu cho con cá này
    mau_ca = random.choice(["orange", "gold", "silver", "yellowgreen", "coral"])
 
    # ---- Thân cá (hình tròn) ----
    nhac_but_toi(x, y)
    rua.setheading(0)
    rua.color("black", mau_ca)
    rua.begin_fill()
    rua.circle(kich_thuoc)
    rua.end_fill()
 
    # Con rùa vẽ vòng tròn bắt đầu từ mép dưới, nên tâm thân cá
    # thực tế nằm CAO HƠN điểm (x, y) một khoảng bằng bán kính.
    # Tính vị trí đó 1 lần, rồi dùng chung cho đuôi và mắt bên dưới.
    y_giua = y + kich_thuoc
 
    # ---- Đuôi cá (tam giác đều nhỏ, gắn phía sau thân) ----
    # Cách vẽ tam giác đều quen thuộc: đi tới rồi rẽ trái 120 độ, lặp lại 3 lần
    nhac_but_toi(x - kich_thuoc, y_giua)
    rua.setheading(200)         # xoay bút chếch ra phía sau thân cá
    rua.fillcolor(mau_ca)
    rua.begin_fill()
    for canh in range(3):
        rua.forward(kich_thuoc)
        rua.left(120)
    rua.end_fill()
 
    # ---- Mắt cá (chấm nhỏ màu đen) ----
    nhac_but_toi(x + kich_thuoc * 0.4, y_giua + kich_thuoc * 0.3)
    rua.dot(4, "black")


# ===== GỌI CÁC HÀM THEO ĐÚNG THỨ TỰ =====
ve_bien()
ve_mat_troi()

# --- Vẽ gợn sóng rải khắp mặt biển (số lượng và vị trí NGẪU NHIÊN) ---
so_song = random.randint(5, 8)          # random.randint(a, b) -> số nguyên ngẫu nhiên từ a đến b
for i in range(so_song):
    x_song = random.randint(-330, 330)
    y_song = random.randint(-150, -50)
    ve_song(x_song, y_song, random.randint(3, 6), "blue")

# --- Vẽ vài con cá bơi dưới biển (số lượng, vị trí, kích thước NGẪU NHIÊN) ---
# Vẽ cá TRƯỚC thuyền để cá nằm "dưới nước", thuyền nổi đè lên trên
so_ca = random.randint(4, 7)
for i in range(so_ca):
    x_ca = random.randint(-320, 320)
    y_ca = random.randint(-250, -30)   # nằm dưới đường mặt biển (y < 0)
    kich_thuoc_ca = random.randint(10, 20)
    ve_ca(x_ca, y_ca, kich_thuoc_ca)

# --- Vẽ 3 chiếc thuyền đánh cá (khác vị trí, khác kích thước) ---
ve_thuyen(-220, 0.7)   # thuyền bên trái, hơi nhỏ (ở xa hơn)
ve_thuyen(0, 1.0)      # thuyền ở giữa, kích thước chuẩn
ve_thuyen(230, 0.55)   # thuyền bên phải, nhỏ nhất (xa nhất)

# --- Vẽ vài chú chim bay trên trời (số lượng và vị trí NGẪU NHIÊN) ---
so_chim = random.randint(3, 5)
for i in range(so_chim):
    x_chim = random.randint(-320, 320)
    y_chim = random.randint(180, 260)
    kich_thuoc_chim = random.randint(8, 16)
    ve_song(x_chim, y_chim, 2)

# Ẩn con rùa và giữ cửa sổ vẽ
rua.hideturtle()
man_hinh.mainloop()