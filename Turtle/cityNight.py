from turtle import *
from random import randint
setup(1000, 700)
title("Night City")
speed(0)
hideturtle()
bgcolor("#06142E")
NUMBER_STARS = 200

tracer(0)

# Draw the stars
# =======================
def star(x, y, size):
    penup()
    goto(x, y)
    pendown()
    dot(size, "white")

for _ in range(NUMBER_STARS):
    star(randint(-500, 500), randint(0, 350), randint(1, 6))
# =======================
# Draw the moon
# =======================
penup()
goto(400, 280)
pendown()
dot(90, "#ded526")

penup()
goto(420, 300)
dot(90, "#06142E")
# =======================
# Draw buildings
def building(x, width, height):
    penup()
    goto(x, -350)
    color("black")
    fillcolor("#20252F")
    setheading(90)

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

    # Draw window
    win_size = randint(4, 6)
    row_space = win_size * 3
    height_space = win_size * 3 + 10
    total_col = width // row_space
    total_row = height // height_space
    for col in range(total_col):
        for row in range(total_row):
            ran = randint(0, 5)
            if ran >= 3:
                penup()
                goto(x + win_size + row_space * col , -350 + row * height_space)
                dot(win_size, "#FFD84D")

# Loop to create random building
x = -500
while x < 500:
    w = randint(40, 120)
    h = randint(100, 500)
    building(x, w, h)

    x += (w + randint(0, 10))

# ===========================
exitonclick()