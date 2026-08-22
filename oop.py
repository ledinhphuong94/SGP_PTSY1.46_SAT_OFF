# from turtle import *

# tur1 = Turtle()
# tur2 = Turtle()
# tur3 = Turtle()
# tur4 = Turtle()

# tur1.speed(100)
# tur1.color("red")
# tur1.shape("turtle")
# tur1.penup()
# tur1.goto(-50, -50)
# tur1.pendown()

# tur2.speed(100)
# tur2.color("blue")
# tur2.shape("square")
# tur2.penup()
# tur2.goto(50, -50)
# tur2.pendown()

# tur3.speed(100)
# tur3.color("green")
# tur3.shape("triangle")
# tur3.penup()
# tur3.goto(50, 50)
# tur3.pendown()

# tur4.speed(100)
# tur4.color("yellow")
# tur4.shape("circle")
# tur4.penup()
# tur4.goto(-50, 50)
# tur4.pendown()


# for i in range(1000):
#     tur1.forward(i * 2 + 5)
#     tur1.left(90)

#     tur2.forward(i * 2 + 5)
#     tur2.left(90)
    
#     tur3.forward(i * 2 + 5)
#     tur3.left(90)

#     tur4.forward(i * 2 + 5)
#     tur4.left(90)

# exitonclick()

# Turtle Race

from turtle import *

speed(0)
pensize(5)
penup()
goto(-400, 300)
pendown()
setup(1000, 800)

for i in range(2):
    forward(800)
    right(90)
    forward(600)
    right(90)

def startRace(t, x, y, color):
    t.color(color)
    t.shape('turtle')
    t.speed(100)
    t.penup()
    t.goto(x, y)

t1 = Turtle()
t2 = Turtle()

# start of the race
startRace(t1, -400, 100, 'red')
startRace(t2, -400, -100, 'blue')


exitonclick()