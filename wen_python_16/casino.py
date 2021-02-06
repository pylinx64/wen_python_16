import random

print("Приветсвую себя в казино!")
while True:
	number_random = random.randint(1, 1)
	#print(number_random)

	number_player = input("Введите случайное число: ")

	if str(number_random) == number_player:
		print("Вы Победили! ")
	if str(number_random) != number_player:
		print("Вы Проиграли! ")
		print(number_random)
	print("----------------------")
