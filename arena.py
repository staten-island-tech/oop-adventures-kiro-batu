import random
## Import the types of troops
from troops import Cavalry, Archer, Infantry

##Import the enemies
from enemies import Slime, Zombie, Goblin, Skeleton, Minotaur, Cyclops, GiantSpider, Yeti, Hydra, nelahWrM
from __archer import  vs_slimea, vs_Goba, vs_zoma, vs_Skelea, vs_Mina, vs_Cyca, vs_hyda, vs_GSa, vs_wrma, vs_yea, slime_defeat, troopslime
from __infantry import   vs_slimei, vs_Gobi, vs_zomi, vs_Skelei, vs_Mini, vs_Cyci, vs_hydi, vs_GSi, vs_wrmi, vs_yei
from __cavalry import vs_slimec, vs_Gobc, vs_zomc, vs_Skelec, vs_Minc, vs_Cycc, vs_hydc, vs_GSc, vs_wrmc, vs_yec

trooplist = ["Cavalry", "Archer", "Infantry" ]
troopinput = ("Select a troop type to send out into battle: ")

def cal():
    print("You have selected the Cavalry: your current stats will be printed ")
    print ("- Attack: ", Cavalry.attack)
    print ("- Speed: ", Cavalry.speed )
    print ("- Health: ", Cavalry.health)
   
def arc():
    print("You have selected the Archer: your current stats will be printed ")
    print ("- Attack: ", Archer.attack)
    print ("- Speed: ", Archer.speed )
    print ("- Health: ", Archer.health)

def inf():
    print("You have selected the Infantry: your current stats will be printed ")
    print ("- Attack: ", Infantry.attack)
    print ("- Speed: ", Infantry.speed )
    print ("- Health: ", Infantry.health)
    
def beforearena():
    print("Before entering the next battle, you're current stats will be shown ")
    print ("- Cavalry: Attack: ", Cavalry.attack)
    print ("- Cavlary: Speed: ", Cavalry.speed )
    print ("- Cavalry: Health: ", Cavalry.health)
    input("---")
    print ("- Archer: Attack: ", Archer.attack)
    print ("- Archer: Speed: ", Archer.speed )
    print ("- Archer: Health: ", Archer.health)
    input("---")
    print ("- Infantry: Attack: ", Infantry.attack)
    print ("- Infantry: Speed: ", Infantry.speed )
    print ("- Infantry: Health: ", Infantry.health)

def slimefight():
    print ("You begin to engage in a battle with the devilish SLIME")
    print ("It's stats will be shown")
    print ("- Attack:", Slime.attack )
    print ("- Speed: ", Slime.speed)
    print ("- Health: ", Slime.health)
    troopinput = input("Select a troop type to send out into battle: ")
    if troopinput == ("Cavalry"):
        cal()
        vs_slimec()
    elif troopinput == ("Archer"):
        arc()
        vs_slimea()
    if troopinput == ("Infantry"):
        inf()
        vs_slimei()
    while len(slime_defeat) == 1:
        print ("---")
        print ("Given you're unfortunate loss, you must try again with a different figure")
        print ("Keep in mind your choose must be different from your first attempt")
        print ("---")
        slimeinput = input("Select another troop type to send out into battle: ")
        if slimeinput == ("Cavalry"):
            vs_slimec()
        elif slimeinput== ("Archer"):
            vs_slimea()
        if slimeinput == ("Infantry"):
            vs_slimei()
        break
    while len(slime_defeat) == 2:
        print ("---")
        print ("This is your final chance you must try again with a different figure")
        print ("Keep in mind your choose must be different from your previous attempt")
        print ("---")
        slimeinput = input("Select another troop type to send out into battle: ")
        if slimeinput == ("Cavalry"):
            vs_slimec()
        elif slimeinput == ("Archer"):
            vs_slimea()
        if slimeinput == ("Infantry"):
            vs_slimei()
        break
    while len(slime_defeat) == 3:
        print ("---")
        print ("You have suffered a tragic loss againt Nelahwrm")
        print ("Your figure are splintered beyond repair ")
        print ("Nelahwrm's reign will continue unphased")
slimefight()

