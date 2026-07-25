from turtle import *
from random import randint

setup(1000, 700)
title("Night City")

speed(0)
hideturtle()
bgcolor("#06142E")
tracer(0)

# ==========================
# Vẽ sao
# ==========================
def star(x, y, size):
    penup()
    goto(x, y)
    dot(size, "white")

for _ in range(180):
    star(randint(-480, 480), randint(0, 330), randint(2, 5))

# ==========================
# Mặt trăng
# ==========================
penup()
goto(320, 220)
dot(90, "#FFF7B2")

goto(340, 235)
dot(80, "#06142E")

# ==========================
# Hàm vẽ tòa nhà
# ==========================
def building(x, width, height):

    penup()
    goto(x, -300)
    setheading(90)

    color("black")
    fillcolor("#20252F")

    begin_fill()

    pendown()
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)

    end_fill()

    # cửa sổ
    for col in range(width // 18):
        for row in range(height // 20):

            if randint(0, 3):

                penup()

                goto(
                    x + 6 + col * 18,
                    -285 + row * 20
                )

                dot(6, "#FFD84D")

# ==========================
# Vẽ thành phố
# ==========================
x = -500

while x < 500:

    w = randint(40, 90)
    h = randint(150, 450)

    building(x, w, h)

    x += w

# ==========================
# Mặt đất
# ==========================
penup()
goto(-500, -300)

fillcolor("#111111")

begin_fill()

pendown()

for _ in range(2):
    forward(1000)
    left(90)
    forward(35)
    left(90)

end_fill()

update()
done()
