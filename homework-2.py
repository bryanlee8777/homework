from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    t=mc.events.pollProjectileHits()
    if len(t)>0:
        hit=t[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        b=mc.getBlock(x,y,z)
        mc.player.setPos(x,y,z)
        mc.spawnEntity(x,y,z,99)
        
        
