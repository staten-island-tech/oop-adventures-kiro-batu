## Import the types of troops
from troops import Cavalry, Archer, Infantry

##Import the blessings
from the_blessings import Hercules, Hermes, Artemis

##Import all the items
from the_armor import Shield, Boots, Cloak, Chestplate

##Import the enemies
from enemies import Slime, Zombie, Goblin, Skeleton, Minotaur, Cyclops, GiantSpider, Yeti, Hydra, nelahWrM

##Import all of the arenas
from arena import picky, beforearena, slimebattle, base_arena, firstboss, Minotaurecounter, Cyclops_Encounter, nextboss, Yeti_Encounter, Hydra_Encounter, finalboss, thefinal_encounter, nelahWrM


print ("---------")
print ("Kato Productions Presents")
print ("BOTS Against the WORLD")
input ("---------")


def storyline():
    print ("The world has been run over by the overlord NelahWrM and his monstrous forces")
    print ("Many have suffered under his evil rule")
    input ("---")
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
    print ("The figure presented you a random attack (15 - 20), a random speed (5 - 20), and a random health (10 - 20)")
    print ("- Attack: ", Archer.attack)
    print ("- Speed: ", Archer.speed )
    print ("- Health: ", Archer.health)
    input ("---")
    input ("Next, he presented you the Infantry:")
    input ("---")
    print ("The figure presented you a random attack (15 - 20), a random speed (5 - 20), and a random health (10 - 20)")
    print ("- Attack: ", Infantry.attack)
    print ("- Speed: ", Infantry.speed )
    print ("- Health: ", Infantry.health)
    input ("---")
    input ("Lastly, he presented you the Cavalry:")
    input ("---")
    print ("The figure presented you a random attack (5 - 20), a random speed (15 - 20), and a random health (10 - 20)")
    print ("- Attack: ", Cavalry.attack)
    print ("- Speed: ", Cavalry.speed )
    print ("- Health: ", Cavalry.health)
intro()

def nextpart():
    input ("---")
    print ("You bid your farwells to the distant man, as you prepared yourself for the mountainous quest you've been assigned ")
    print ("The strange man had informed you that the first of NelahWrm's strongholds was the ominous Swampy Swamp")
    input ("---")
    print ("As you approached the dark swamp a feeling of immense dread overcame you")
    print ("The power of NelahWrm was oozing all over")
    input ("---")
    print ("As you entered the swamp the thick substance clinged to your legs dragging you down in the process")
    input ("---")
    print ("Each step was a struggle and the first of NelahWrm's servants emerged from the swamp, The SLIME.")
nextpart()

def firstbattle():
    input ("---")
    print ("As you scrambled to find your footing you fumbled through your sack to find your figures")
    print ("You're fingers felt the soft wooden figures; you returned to a sense of indomitable focus")
    input ("---")   
    beforearena()
    input ("---")
    slimebattle()
    
firstbattle()