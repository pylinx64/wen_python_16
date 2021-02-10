import random
import time

list_lot = ["PS5", "Minecraft", "Potate", "House", "Car"]
fishki = 0

print("< Лото-забава: выиграй 10 Potate! >")
time.sleep(0.5)
print("Вы можете выйграть: ")
time.sleep(0.5)
print(list_lot)
time.sleep(0.5)
print("У вас 1000$")
time.sleep(0.5)

while fishki < 5:
	fishki = fishki + 1
	prize = random.choice(list_lot)
	print("Ваш  - ", prize)
	time.sleep(0.5)h

print("У вас 0$")
time.sleep(0.5)

	

