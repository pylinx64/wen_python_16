import time
import turtle
from random import randrange

BREAK_FLAG = False

# сохраняем экран в переменную
screen = turtle.Screen()
# название окошка
screen.title('Snake_v2.0')
# меняем цвет заднего фона
screen.bgcolor('orange')
# размер экрана
screen.setup(650, 650)
screen.tracer(0)

# список для змейки
snake = []
# создаем голову змейки и ложим в список snake
snake_segment = turtle.Turtle()
snake_segment.shape('square')
snake_segment.penup()
snake.append(snake_segment)

# управление
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
# слушает клавиши
screen.listen()

# делаем еду
food = turtle.Turtle()
food.shape('circle')
food.penup()
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))

while True:
	# если расстояние от головы до еды меньше 10
    if snake[0].distance(food) < 10:
		# телепортируем еду рандомно
        food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
        # создем сегмент змейки
        snake_segment = turtle.Turtle()
        # меняем форму змейки на квадрат
        snake_segment.shape('square')
        # меняем цвет змейки
        snake_segment.color('gray')
        # убираем карандаш (чтобы не было линий)
        snake_segment.penup()
        # добавляем сегмент звейки в змейку
        snake.append(snake_segment)

	# передвигаем тело змеи с помощью цикла 
    for i in range(len(snake)-1, 0, -1):
		# забираем координаты х у 
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        # ставим тело в х у
        snake[i].goto(x, y)
	
	# двигаем змейку
    snake[0].forward(20)

	# обновляем экран
    screen.update()
    
    #----------------------вы находитесь тут-----------------------
    x_snake = snake[0].xcor()
    y_snake = snake[0].ycor()
    
    # x - это левая и правая стена
    if x_snake > 300:
        screen.bgcolor('red')
        break
    elif x_snake < -300:
        
        break
    elif y_snake < -300:
        
        break
    elif y_snake > 300:
        
        break
    #----------------------вы находитесь тут-----------------------
    
	# фпс
    time.sleep(0.15)

# запуск 
screen.mainloop()
