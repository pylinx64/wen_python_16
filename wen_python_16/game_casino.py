# импорт библиотеки для рандома
import random 

while True:
	print()
	print("$$$	Приветсвую тебя в казино!	$$$")

	# храним случайное число ПК
	number_random = random.randint(1, 10)

	# пользователь вводит число
	number_player = input("Введите число (от 1 до 10) -> ")

	# проверка и вополнение условия победы или поражения
	if str(number_random) == number_player:
		# блок1 работает если мы выиграем
		print("		You Win!!!	")
	
	elif number_player == 'q':
		# блок2 отсанавливает игру (бесконечный цикл)
		print("!!!	Игра остановлена	!!!")
		break
	
	else:
		# блок3 работает если мы проиграем
		print("		Game over	")
		print(number_random)
