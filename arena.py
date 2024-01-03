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
<<<<<<< HEAD
    else:
        print ("This was not one of the options. Remember, the choice must be first letter capital.")
        return slimebattle()
=======

def nextarena():
    troopinput = ["Cavalry", "Archer", "Infantry"]
    print ("After you're simple introduction, courtesy of the Slime, you will now engage in more proper fights")
    
    start = 1
    end = 4
    
    values = list(range(start,end))
    mon_choice = random.choice(values)

    if mon_choice == (1):
        print ("You've engaged in a battle with a demonic ZOMBIE")
        print ("---")
        print ("Attack:", Zombie.attack)
        print ("Speed:", Zombie.speed)
        print ("Health:", Zombie.health)
    elif mon_choice == (2):
        print ("You've engaged in a battle with a ghastly SKELETON")
        print ("---")
        print ("Attack:", Skeleton.attack)
        print ("Speed:", Skeleton.speed)
        print ("Health:", Skeleton.health)
    if mon_choice == (3):
        print ("You've engaged in a battle with a cheeky GOBLIN")   
    while len(slime_defeat) == 1:
        print ("---")
        print ("Attack:", Goblin.attack)
        print ("Speed:", Goblin.speed)
        print ("Health:", Goblin.health)
    
    troopinput = input("Select a troop type to send out into battle: ")

    while troopinput == ("Cavalry"):
        print("---")
        cal()
        if mon_choice == (1):
            print("---")
            vs_Gobc
        if mon_choice == (2):
            print("---")
            vs_zomc
        if mon_choice == (3):
            print("---")
            vs_Skelec

    while troopinput == ("Archer"):
        print("---")
        arc()
        if mon_choice == (1):
            print("---")
            vs_Goba
        if mon_choice == (2):
            print("---")
            vs_zoma
        if mon_choice == (3):
            print("---")
            vs_Skelea

    while troopinput == ("Infantry"):
        print("---")
        inf()
        if mon_choice == (1):
            print("---")
            vs_Gobi
        if mon_choice == (2):
            print("---")
            vs_zomi
        if mon_choice == (3):
            print("---")
            vs_Skelei

def minoboss():
    print("You've encountered your first boss, traveler")
and



    
    
    

>>>>>>> 3e4bf7a70b28b6a7753e1b97defcf8035cd154e9
