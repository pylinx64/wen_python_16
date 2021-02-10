import turtle
import random

colors = ['#800000', '#E6FF2B', '#009708', '#30F6FF', '#0B006A', '#FF32C0']
t = turtle.Pen()
turtle.bgcolor('black')

for despasito2 in range(1000):
	t.pencolor(colors[despasito2%6])
	t.penup()
	t.forward(random.randint(0, 100))
	t.left(random.randint(0, 360))
	t.pendown()
	t.circle(random.randint(1, 20))
	

	
	
