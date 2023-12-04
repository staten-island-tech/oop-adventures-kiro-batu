from archers import Archer
from enemies import Slimes

Archer.ArcherAttack()
Slimes.SlimeAppear()
winny = []

def compare():
    if Archer.ArcherAttack > Slimes.SlimeAppear:
        print ("You have won this battle good luck in the next")
        winny.append("1")
compare()
