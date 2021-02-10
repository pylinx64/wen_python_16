import turtle

list_colors = ['#26E03C', '#26B0E0', '#E026B9', '#E0E026']
t = turtle.Pen()
turtle.bgcolor('black')

text_paint = turtle.textinput('Что рисовать?', 'Введите текст:')

for x in range(1000):
	t.pencolor(list_colors[x%4])
	t.penup()
	t.forward(x*4)
	t.pendown()
	t.write(text_paint, font = ('Arial', int((x + 4) / 4), 'bold'))
	t.left(72)
