from turtle import *
from random import *

# Thiet lap man hinh
setup(700, 500)
bgcolor("skyblue")
title("Doan thuyen danh ca")
speed(0)
hideturtle()

def move_pen_to(x, y):
    penup()
    goto(x, y)
    pendown()

def draw_sea():
    move_pen_to(-350, 0)
    color("dodgerblue")
    begin_fill()
    for i in range(2):
        forward(700)
        right(90)
        forward(250)
        right(90)
    end_fill()

def draw_sun(x, y):
    move_pen_to(x, y)
    color("gold")
    begin_fill()
    circle(40)
    end_fill()

def draw_wave(x,y, number=5, color="white"):
    move_pen_to(x, y)
    setheading(0)
    color(color)
    pensize(2)
    for i in range(number):
        pass

draw_sea()
draw_sun(randint(-300, 300), 150)
exitonclick()