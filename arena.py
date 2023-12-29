import random
## Import the types of troops
from troops import Cavalry, Archer, Infantry

##Import the enemies
from enemies import Slime, Zombie, Goblin, Skeleton, Minotaur, Cyclops, GiantSpider, Yeti, Hydra, nelahWrM
from __archer import   vs_slimea, vs_Goba, vs_zoma, vs_Skelea, vs_Mina, vs_Cyca, vs_hyda, vs_GSa, vs_wrma, vs_yea
from __infantry import   vs_slimei, vs_Gobi, vs_zomi, vs_Skelei, vs_Mini, vs_Cyci, vs_hydi, vs_GSi, vs_wrmi, vs_yei
from __cavalry import vs_slimec, vs_Gobc, vs_zomc, vs_Skelec, vs_Minc, vs_Cycc, vs_hydc, vs_GSc, vs_wrmc, vs_yec

trooplist = ["Cavalry", "Archer", "Infantry" ]


troopinput = ("Select a troop type to send out into battle: ")

def picky():
    input(troopinput)
    print("---")
    if troopinput == ("Cavalry"):
        print("You have selected the Cavalry: your current stats will be printed ")
        print ("- Attack: ", Cavalry.attack)
        print ("- Speed: ", Cavalry.speed )
        print ("- Health: ", Cavalry.health)
    elif troopinput == ("Archer"):
        print("You have selected the Archer: your current stats will be printed ")
        print ("- Attack: ", Archer.attack)
        print ("- Speed: ", Archer.speed )
        print ("- Health: ", Archer.health)
    if troopinput == ("Infantry"):
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
    
    print ("You've enagaged in a battle with a devilish slime")
    print ("- The SLIME's attack stat is", Slime.attack)
    print ("- The SLIME's health stat is", Slime.health)
    print ("- The SLIME's speed stat is", Slime.speed)
    
    print ("---")
    troopinput = input("Select a troop type to send out into battle: ")
    

    if troopinput == ("Cavalry"):
        print("You have selected the Cavalry: your current stats will be printed ")
        print ("---")
        print ("- Attack: ", Cavalry.attack)
        print ("- Speed: ", Cavalry.speed )
        print ("- Health: ", Cavalry.health)
    elif troopinput == ("Archer"):
        print ("---")
        print("You have selected the Archer: your current stats will be printed ")
        print ("- Attack: ", Archer.attack)
        print ("- Speed: ", Archer.speed )
        print ("- Health: ", Archer.health)
    if troopinput == ("Infantry"):
        print("You have selected the Infantry: your current stats will be printed ")
        print ("---")
        print ("- Attack: ", Infantry.attack)
        print ("- Speed: ", Infantry.speed )
        print ("- Health: ", Infantry.health)

    
    while troopinput == ("Cavalry"):
        input ("You have picked the cavalry:")
        print ("---")
        vs_slimec()
        break


    while troopinput == ("Archer"):
        input ("You have picked the archer:")
        print ("---")
        vs_slimea()
        break
    
    while troopinput == ("Infantry"):
        input ("You have picked the infantry:")
        print ("---")
        vs_slimei()
        break

def base_arena(): 
    start = 1
    end = 4
    values = list(range(start,end))
    choice = random.choice(values)
    if choice == (1):
        print ("You've engaged in a battle with a demonic ZOMBIE")
        print ("---")
        print ("Attack:", Zombie.attack)
        print ("Speed:", Zombie.speed)
        print ("Health:", Zombie.health)
    elif choice == (2):
        print ("You've engaged in a battle with a ghastly SKELETON")
        print ("---")
        print ("Attack:", Skeleton.attack)
        print ("Speed:", Skeleton.speed)
        print ("Health:", Skeleton.health)
    if choice == (3):
        print ("You've engaged in a battle with a cheeky GOBLIN")   
        print ("---")
        print ("Attack:", Goblin.attack)
        print ("Speed:", Goblin.speed)
        print ("Health:", Goblin.health)
    

    troopinput = input("Select a troop type to send out into battle: ")

    if troopinput == ("Cavalry"):
        print("You have selected the Cavalry: your current stats will be printed ")
        print ("- Attack: ", Cavalry.attack)
        print ("- Speed: ", Cavalry.speed )
        print ("- Health: ", Cavalry.health)
    elif troopinput == ("Archer"):
        print("You have selected the Archer: your current stats will be printed ")
        print ("- Attack: ", Archer.attack)
        print ("- Speed: ", Archer.speed )
        print ("- Health: ", Archer.health)
    if troopinput == ("Infantry"):
        print("You have selected the Infantry: your current stats will be printed ")
        print ("- Attack: ", Infantry.attack)
        print ("- Speed: ", Infantry.speed )
        print ("- Health: ", Infantry.health)
    
    while troopinput == ("Cavalry"):
        input ("You have picked the cavalry, its updated stats will be shown")
        print ("---")
        if choice == (1):
            vs_zomc()
        elif choice == (2):
            vs_Skelec
        if choice == (3):
            vs_Gobc
        break

    while troopinput == ("Archer"):
        input ("You have picked the archer, its updated stats will be shown")
        print ("---")
        if choice == (1):
            vs_zoma()
        elif choice == (2):
            vs_Skelea
        if choice == (3):
            vs_Goba
        break
    
    while troopinput == ("Infantry"):
        input ("You have picked the infantry, its updated stats will be shown")
        print ("---")
        if choice == (1):
            vs_zomi()
        elif choice == (2):
            vs_Skelei
        if choice == (3):
            vs_Gobi
        break



    
def firstboss():
    print ("You've encountered your first BOSS.")

def Minotaurecounter():
    print ("You've encountered a mighty MINOTAUR")
    print ("---")
    print (Minotaur.attack)
    print (Minotaur.speed)
    print (Minotaur.health)

def Cyclops_Encounter():
    print ("You've encountered a brutal CYCLOPS ")
    print ("---")
    print (Cyclops.attack)
    print (Cyclops.speed)
    print (Cyclops.health)

def nextboss():
    print ("You've encountered your second group of BOSSES.")

def GS_Encounter():
    print ("You've encountered the menacing GIANT SPIDER")
    print ("---")
    print (GiantSpider.attack)
    print (GiantSpider.speed)
    print (GiantSpider.health)

def Yeti_Encounter():
    print ("You've encountered a ... yellow YETI")
    print ("---")
    print (Yeti.attack)
    print (Yeti.speed)
    print (Yeti.health)

def Hydra_Encounter():
    print ("You've encountered a HORRIBLE HYDRA")
    print ("---")
    print (Hydra.attack)
    print (Hydra.speed)
    print (Hydra.health)

def finalboss():
    print ("You've encountered the final boss.")

def thefinal_encounter():
    print ("You've encountered THE ALMIGHTY NELAHWRM")
    print ("---")
    print (nelahWrM.attack)
    print (nelahWrM.speed)
    print (nelahWrM.health)