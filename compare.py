##import your troops 
from cavalry import Cavalry
from infantry import Infantry
from archers import Archer

##import all enemies
from enemies import Slimes
from enemies import Zombies
from enemies import Goblins
from enemies import Skeleton
from enemies import Minotaur
from enemies import Yeti
from enemies import GiantSpider
from enemies import Cyclops
from enemies import Hydra
from enemies import nelahWrM

def compareArcher():
    print ("Here is the Slime's Attack: ", Slimes.slimeattack)
    print ("Here is the Archer's Attack: ", Archer.ArcherAttack)
    if Slimes.slimeattack < Archer.ArcherAttack:
        print ("You won the stat")
compareArcher()

print (Archer.ArcherAttack)