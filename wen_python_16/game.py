# импортируем библиотеку pygame
import pygame

# инициализировать игровой движок
pygame.init()

# цвета по умолчанию
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)
blue =  ( 0,     0, 255)

# добавим число пи
pi = 3.141592653

# открываем окно с заданными параметрами
size = [800, 600]
screen = pygame.display.set_mode(size)

# заголовок окна
pygame.display.set_caption("ITFriends v2.0")

# основная программа
# оставаться в цикле пока пользователь не нажмет кнопку закрытия окна
done = False

# для контроля FPS
clock = pygame.time.Clock()

#------------ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ------------------
while done==False:
	# ОБРАБОТКА СОБЫТИЙ 
	# Отслеживаем кнопки и закрываем окно
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	# ОБРАБОТКА СОБЫТИЙ 
	
	
	# ВСЯ ИГРОВАЯ ЛОГИКА
	
	# ВСЯ ИГРОВАЯ ЛОГИКА
	
	
	# КОД ДЛЯ РИСОВАНИЯ
	# Заливает фон
	screen.fill(black)
	
	# прямоугольник
	pygame.draw.rect(screen, white, [rect_x, 50, 50, 50])
	
	# меняем координату прямоугольника х
	rect_x = rect_x + rect_speed_x
	
	# границы
	if rect_x > 800:
		rect_speed_x = rect_speed_x * -1
	
	# КОД ДЛЯ РИСОВАНИЯ
	
	# Обновляет экран
	pygame.display.flip()
	
	# ограничивает до 60 кадров в секунду (FPS)
	clock.tick(60)

# Правильно закрываем pygame
pygame.quit()
