from turtle import *

t = Turtle()
t.color('blue')
t.shape('circle')
t.pendown()
t.speed(100)

def draw(x, y):
    print(x, y)
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def setGreen():
    t.color('green')

def setBlue():
    t.color('blue')

scr = t.getscreen()
# mouse event
scr.onscreenclick(move)
t.ondrag(draw)
    
# keyboard event
# tell scr object listen to keyboard events
scr.listen()
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'b')

mainloop()