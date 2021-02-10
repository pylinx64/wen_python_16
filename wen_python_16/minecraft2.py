from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

# координаты игрока - клавиша F3
x = 166
y = 72
z = 30
block = 0

for y in range(72, 0, -1):
	# команда для вставки блока
	mc.setBlock(x, y, z, block)
	time.sleep(0.3)

