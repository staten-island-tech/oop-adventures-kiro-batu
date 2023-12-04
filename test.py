from cavalry import Cavalry
from enemies import Slimes

winny = []

def compare():
    if Cavalry.CavalryAttack > Slimes.SlimeAppear():
        print ("You have won this battle good luck in the next")
        winny.append("1")
compare()
