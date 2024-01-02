import random
## Import the types of troops
from troops import Cavalry, Archer, Infantry

##Import the enemies
from enemies import Slime, Zombie, Goblin, Skeleton, Minotaur, Cyclops, GiantSpider, Yeti, Hydra, nelahWrM
from __archer import  vs_slimea, vs_Goba, vs_zoma, vs_Skelea, vs_Mina, vs_Cyca, vs_hyda, vs_GSa, vs_wrma, vs_yea, slime_defeat, troopslime
from __infantry import   vs_slimei, vs_Gobi, vs_zomi, vs_Skelei, vs_Mini, vs_Cyci, vs_hydi, vs_GSi, vs_wrmi, vs_yei, slime_defeat, troopslime
from __cavalry import vs_slimec, vs_Gobc, vs_zomc, vs_Skelec, vs_Minc, vs_Cycc, vs_hydc, vs_GSc, vs_wrmc, vs_yec, slime_defeat, troopslime

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

def slimebattle():
    trooplist = ["Cavalry", "Archer", "Infantry" ]
    print ("You're know engaged within a battle with the devilish SLIME")
    print("---")
    print("Slime: Attack: ", Slime.attack)
    print("Slime: Speed:", Slime.speed)
    print("Slime: Health: ", Slime.health)
    troopinput = input("Select a troop type to send out into battle: ")
    if troopinput == ("Cavalry"):
        print("---")
        cal()
        print("---")
        vs_slimec()
    elif troopinput == ("Archer"):
        print("---")
        arc()
        print("---")
        vs_slimea()
    if troopinput == ("Infantry"):
        print("---")
        inf()
        print("---")
        vs_slimei()


    
    
    

