import time
import turtle
from random import randrange

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
food.color('#4427AD')
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))

# переменная-флаг
FLAG = False

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
        #turtle.write()
        break
    elif x_snake < -300:
        screen.bgcolor('red')
        break
    # y - это верхняя и нижняя
    elif y_snake < -300:
        screen.bgcolor('red')
        break
    elif y_snake > 300:
        screen.bgcolor('red')
        break
    #----------------------вы находитесь тут-----------------------
    
    # game over если кушает себя
    for body in snake[1:]:
        # берем координаты туловища
        coordinates = body.position()
        # проверяем расстояние от туловища до головы
        if snake[0].distance(coordinates) < 10:
            # если расстояние меньше 10 то меняем флажок
            FLAG = True
    
    # голова коснулась туловища, game over
    if FLAG == True:
        screen.bgcolor('red')
        break
    
	# фпс
    time.sleep(0.1)

# запуск 
screen.mainloop()
