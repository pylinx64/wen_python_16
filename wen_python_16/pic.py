import turtle

t = turtle.Pen()
colors = ["#456EB4", "#B4454C",  "#B4B245", "#45B487", "#744D6C", "#A01215"]
turtle.bgcolor("black")

# храним в "коробочке" текст
text = turtle.textinput("Введите текст1", "Введите текст2")


# Спиралька
for x in range(1000):
	t.pencolor(colors[x%6])
	t.penup()
	t.forward(x)
	t.pendown()
	t.write(text)
	# от 0 до 180
	t.left(67)


# Останавливает программу
turtle.done()
