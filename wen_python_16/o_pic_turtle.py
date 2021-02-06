import turtle

# карандаш
t = turtle.Pen()

# цвета
colors = ["#800000", "#1A8000", "#42D3FC", "#8C42FC"]

# задний фон
turtle.bgcolor("black")


t.pencolor(colors[1])
# прямая линия
t.forward(180)
# угол
t.left(120)

t.circle(40)

# не закрывает программу
turtle.done()

