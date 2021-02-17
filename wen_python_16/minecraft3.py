from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
block = 46
for y in range(50, 250):
	if y % 2 == 0:
		mc.setBlock(x, y, z, 152)
	else:
		mc.setBlock(x, y, z, 46)
	
