import turtle

t = turtle.Pen()

colors = ['#F80016', '#EC00F8', '#00F8EC', '#00F807']
turtle.bgcolor('white')

def rect(x):
	'''Рисует сторону и поворачивает'''
	t.forward(100)
	t.left(x)

# ставит черепашку вместо карандаша
t.shape('turtle')

for x in range(100):
	rect(67)

turtle.done()
