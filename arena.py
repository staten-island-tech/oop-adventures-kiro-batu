import random
## Import the types of troops
from troops import Cavalry, Archer, Infantry

##Import the enemies
from enemies import Slime, Zombie, Goblin, Skeleton, Minotaur, Cyclops, GiantSpider, Yeti, Hydra, nelahWrM

trooplist = ["Cavalry", "Archer", "Infantry" ]

def picky():
    troopinput = input("Select a troop type to send out into battle: ")
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
    

def base_arena():
    start = 1
    end = 4
    values = list(range(start,end))
    choice = random.choice(values)
    if choice == (1):
        print ("You've encountered a demonic ZOMBIE")
        print ("---")
        print (Zombie.attack)
        print (Zombie.speed)
        print (Zombie.health)
    elif choice == (2):
        print ("You've encountered a ghastly SKELETON")
        print ("---")
        print (Skeleton.attack)
        print (Skeleton.speed)
        print (Skeleton.health)
    if choice == (3):
        print ("You've encountered a cheeky GOBLIN")   
        print ("---")
        print (Goblin.attack)
        print (Goblin.speed)
        print (Goblin.health)
    
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