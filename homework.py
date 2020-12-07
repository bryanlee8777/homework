from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    b = mc.getBlock(x,y-1,z)
    if b == 2:mc.setBlock(x,y,z,38)