# импортируем библиотеку pygame
import pygame

# инициализировать игровой движок
pygame.init()

# цвета по умолчанию
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)


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
	screen.fill(white)
	
	# прямая линия
	pygame.draw.line(screen, red, [4, 6], [800, 600], 15)
	pygame.draw.line(screen, red, [800, 6], [4, 600], 15)
	
	# несколько линий
	for y_offset in range(0, 100, 10):
		pygame.draw.line(screen, (55, 55, 234), [0, 10+y_offset], [100, 110+y_offset], 5)
	# КОД ДЛЯ РИСОВАНИЯ
	
	# Обновляет экран
	pygame.display.flip()
	
	# ограничивает до 60 кадров в секунду (FPS)
	clock.tick(60)

# Правильно закрываем pygame
pygame.quit()
