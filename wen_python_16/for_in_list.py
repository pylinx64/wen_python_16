import time, colorama
from colorama import Fore, Back, Style
colorama.init()

for i in range(0, 100):
	print(Back.WHITE + Fore.BLACK + 'Vzlom, ', i, '%')
	time.sleep(0.3)
