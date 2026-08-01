"""
VE CANH DONG QUE DON GIAN BANG TURTLE
Ban rut gon - de doc, de hieu tung dong lenh
"""

import turtle

# ===== THIET LAP =====
man_hinh = turtle.Screen()
man_hinh.bgcolor("skyblue")

rua = turtle.Turtle()
rua.speed(0)


def ve_hinh_chu_nhat(x, y, rong, cao, mau):
    """Ve hinh chu nhat, goc duoi-trai la (x, y)"""
    rua.penup()
    rua.goto(x, y)
    rua.setheading(0)
    rua.pendown()
    rua.fillcolor(mau)
    rua.begin_fill()
    for i in range(2):
        rua.forward(rong)
        rua.left(90)
        rua.forward(cao)
        rua.left(90)
    rua.end_fill()


def ve_hinh_tron(x, y, ban_kinh, mau):
    """Ve hinh tron, tam phia tren diem (x, y) mot khoang ban_kinh"""
    rua.penup()
    rua.goto(x, y)
    rua.setheading(0)
    rua.pendown()
    rua.fillcolor(mau)
    rua.begin_fill()
    rua.circle(ban_kinh)
    rua.end_fill()


def ve_mai_nha(x_giua, y_day, rong, cao, mau):
    """Ve mai nha hinh tam giac, dinh nhon o giua, huong len tren"""
    rua.penup()
    rua.goto(x_giua - rong / 2, y_day)
    rua.setheading(0)
    rua.pendown()
    rua.fillcolor(mau)
    rua.begin_fill()
    rua.goto(x_giua, y_day + cao)       # len dinh nhon
    rua.goto(x_giua + rong / 2, y_day)  # xuong goc phai
    rua.goto(x_giua - rong / 2, y_day)  # ve lai goc trai
    rua.end_fill()


# ===== VE CANH VAT =====

# bau troi da co san (mau nen), gio ve mat troi
ve_hinh_tron(300, 200, 40, "yellow")

# co dong (mat dat mau xanh)
ve_hinh_chu_nhat(-400, -150, 800, 150, "forestgreen")

# ngoi nha: than nha + mai nha + cua
ve_hinh_chu_nhat(-100, -50, 140, 100, "wheat")       # than nha
ve_mai_nha(-30, 50, 160, 70, "firebrick")            # mai nha
ve_hinh_chu_nhat(-40, -50, 35, 60, "saddlebrown")    # cua ra vao

# cay: than + tan la
ve_hinh_chu_nhat(150, -50, 12, 60, "saddlebrown")    # than cay
ve_hinh_tron(156, 45, 30, "darkgreen")               # tan la

# ===== HOAN THANH =====
rua.hideturtle()
man_hinh.mainloop()