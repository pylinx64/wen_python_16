import turtle
import time

t=turtle.Pen()

def side():
	'''Рисует сторону разного цвета и поворачивает стрелку'''
	t.pencolor('red')
	t.forward(20)
	t.left(5)

i = 0
while i < 72:
	side()
	i = i + 1

time.sleep(1000)
