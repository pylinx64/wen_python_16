import turtle
import time

t = turtle.Pen()
colors = ['lime', '#C35A62', '#9CC35A', '#5AC3B7', '#C35AB8']
turtle.bgcolor('black')

t.pencolor(colors[2])
t.circle(100)

t.left(320)
t.forward(200)
t.circle(100)

time.sleep(50)

