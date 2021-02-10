from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x = 250
y = 85
z = 300

time.sleep(3)
mc.player.setTilePos(x, y, z)
