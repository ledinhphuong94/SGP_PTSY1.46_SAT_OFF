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
from random import randint
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

def celebrate(t):
    t.goto(0, 0)
    t.pendown()
    for i in range(200):
        t.forward(i * 2 + 5)
        t.left(90)

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

# start of the race
startRace(t1, -400, 100, 'red')
startRace(t2, -400, 0, 'blue')
startRace(t3, -400, -100, 'yellow')

def anGian(t):
    print('click!')
    t.forward(-5)
t1.onclick(lambda x, y: anGian(t1))
t2.onclick(lambda x, y: anGian(t2))
t3.onclick(lambda x, y: anGian(t3))
while t1.xcor() < 400 and t2.xcor() < 400 and t3.xcor() < 400:
    ranNum = randint(0, 2)
    if ranNum == 0:
        t1.forward(randint(-2, 7))
        t2.forward(randint(-2, 7))
        t3.forward(randint(-2, 7))
    elif ranNum == 1:
        t2.forward(randint(-2, 7))
        t1.forward(randint(-2, 7))
        t3.forward(randint(-2, 7))
    else:
        t3.forward(randint(-2, 7))
        t2.forward(randint(-2, 7))
        t1.forward(randint(-2, 7))
winNum = max(t1.xcor(), t2.xcor(), t3.xcor())
# check who win
if t1.xcor()== winNum:
    # t1 win
    celebrate(t1)
    t1.write("I win hehe!", font=('Arial', 16, 'bold'))
elif t2.xcor() == winNum:
    # t2 win
    celebrate(t2)
    t2.write("I win hehe!", font=('Arial', 16, 'bold'))
elif t3.xcor() == winNum:
    # draw
    celebrate(t3)
    t3.write("I win hehe!", font=('Arial', 16, 'bold'))


exitonclick()