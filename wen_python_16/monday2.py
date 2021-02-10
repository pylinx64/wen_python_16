import time
import random

targetArray = ["I", "T", "F", "r", "i", "e", "n", "d", "s"]
stringArray = ["", "", "", "", "", "", "", "", ""]

i = 0
while i < len(targetArray):
	if stringArray[i] != targetArray[i]:
		stringArray[i] = chr(random.randint(32, 126))
		
	if stringArray[i] == targetArray[i]:
		i = i + 1
		
	print("\r", end='')
	
	z = 0
	while z < len(stringArray):
		print(stringArray[z], end='')
		z = z + 1
		
	time.sleep(.01)
	
