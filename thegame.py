## Import the types of troops
import cavalry
import archers
import infantry

##Import the blessings
import demblessings

##Import all the items
import armor

##Import the enemies
import enemies
print (enemies) 


print ("---------")
print ("Kato Productions Presents")
print ("BOTS Against the WORLD")
input ("---------")


def storyline():
    print ("The world has been run over by the overlord NelahWrM and his monstrous forces")
    print ("It is now your task to bring his tryanny to its knees")
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
    from archers import rundown
    return rundown