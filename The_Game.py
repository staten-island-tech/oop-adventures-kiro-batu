## Import the types of troops
from troops import Cavalry
from troops import Archer
from troops import Infantry 

##Import the blessings
from the_blessings import Hercules
from the_blessings import Hermes
from the_blessings import Artemis

##Import all the items
from the_armor import Shield
from the_armor import Boots
from the_armor import Cloak
from the_armor import Chestplate

##Import the enemies
from enemies import Slime
from enemies import Skeleton
from enemies import Zombie
from enemies import Goblin
from enemies import Minotaur
from enemies import Cyclops
from enemies import GiantSpider
from enemies import Yeti
from enemies import Hydra
from enemies import nelahWrM


##Variables
import random

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
    start = 1
    end = 3
    values = list(range(start,end))
    choice = random.choice(values)


    print ("You've encountered your first BOSS, the mighty MINOTAUR")
    print ("---")
    print (Minotaur.attack)
    print (Minotaur.speed)
    print (Minotaur.health)

def Minotaurecounter():
    print ("You've encountered a mighty MINOTAUR")
    print ("---")
    print (Minotaur.attack)
    print (Minotaur.speed)
    print (Minotaur.health)

def Cyclops():
    print ("You've encountered a brutal CYCLOPS ")
    print ("---")
    print (Cyclops.attack)
    
def nextboss():
    print ("You've encountered your next BOSS, the menacing GIANT SPIDER")
    print ("---")
    print (GiantSpider.attack)
    print (GiantSpider.speed)
    print (GiantSpider.health)
    

     






print ("---------")
print ("Kato Productions Presents")
print ("BOTS Against the WORLD")
input ("---------")


def storyline():
    print ("The world has been run over by the overlord NelahWrM and his monstrous forces")
    print ("Many have suffered under his evil rule")
    print ("The poor continue to be oppressed as they live their destitute lives")
    print ("Yet the wealthy live in luxury ")
    input ("---")
    print ("Many have attempted to revolt against NelahWrM")
    print ("Yet no one could match the devilish power of NelahWrM")
    input ("---")
    print ("The pioneers of resistance have left a lasting mark of hope")
    print ("It is now your task to bring his tryanny to its knees, as those past tried to do so")
    input ("---")
    print ("As the shady, strange man, dressed in violet, explained this valiant quest he presented you three figures ")
    input ("---")
    print ("The first was a posse of lanky men. They possessed long bows half their size")
    print ("The second was a troup of gruff individuals. They wielded monstrous blades")
    print ("The last were a formation of majestic horses and skilled riders")
    input ("---")
    print ("The figures could come alive and take the form of archers, infantry and cavalry")
    print ("Each figure possessed their own skill set which was nicely divided into three main stats")
    print ("These stats were health, attack and speed")
    input ("---")
    print ("Yet these stats were random courtesy of the man who carved them")
storyline()

def intro():
    input ("---")
    print ('The distant man was kind enough to offer you these figure for his journey had long ended')
    input ("---")
    input ("He presented you the Archer:")
    input ("---")
    print ("The figure presented you a random attack (10 - 50), a random speed (1 - 40), and a random health (1 - 40)")
    print ("- Attack: ", Archer.attack)
    print ("- Speed: ", Archer.speed )
    print ("- Health: ", Archer.health)
    input ("---")
    input ("Next, he presented you the Infantry:")
    input ("---")
    print ("The figure presented you a random attack (15 - 50), a random speed (5 - 40), and a random health (10 - 40)")
    print ("- Attack: ", Infantry.attack)
    print ("- Speed: ", Infantry.speed )
    print ("- Health: ", Infantry.health)
    input ("---")
    input ("Lastly, he presented you the Cavalry:")
    input ("---")
    print ("The figure presented you a random attack (1 - 40), a random speed (15 - 60), and a random health (1 - 50)")
    print ("- Attack: ", Cavalry.attack)
    print ("- Speed: ", Cavalry.speed )
    print ("- Health: ", Cavalry.health)
intro()

def nextpart():
    input ("---")
    print ("You said your farwells to the distant man, as you prepared yourself for the mountainous quest you've been assigned ")
    print ("The strange man had informed you that the first of NelahWrm's strongholds was the ominous Swampy Swamp")
    input ("---")
    print ("As you approached the dark swamp a feeling of immense dread overcame you")
    print ("The power of NelahWrm was oozing all over")
    input ("---")
    print ("As you entered the swamp the thick substance clinged to your legs dragging you down in the process")
    print ("---")
    print ("As you suffered with each step the first of NelahWrm's servants emerged from the swamp, The SLIME.")
nextpart()

def firstbattle():
    input ("---")
    input ("You've encountered a devilish SLIME")
    print ("The SLIME's attack stat is", Slime.attack)
    print ("The SLIME's health stat is", Slime.health)
    print ("The SLIME's speed stat is", Slime.speed)
    input ('---')
    picky()
firstbattle()
