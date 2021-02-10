import time 
import random

targetArray = ["х", "е", "л", "л", "о", " ", "в", "о", "р", "л", "д", "!"]
stringArray = ["", "", "", "", "", "", "", "", "", "", "", ""]

i = 0
while i < len(targetArray):
	if stringArray[i] != targetArray[i]:
		stringArray[i] = chr(random.randint(0, 256))
		
	if stringArray[i] == targetArray[i]:
		i += 1
		
	print('\r', end='')
	z=0
	while z < len(stringArray):
		print(stringArray[z], end='')
		z += 1
		
	time.sleep(.01)

