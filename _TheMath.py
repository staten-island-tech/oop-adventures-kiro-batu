from troops import Archer
from enemies import Slime, Zombie, Goblin, Skeleton, Minotaur, Cyclops, GiantSpider, Yeti, Hydra, nelahWrM


print ("Dont worry about the number above")

def vs_slime():

    print ("You have found a Slime, good luck in this battle")

    slime_listy = []

    input ("---")

    print ("Here is your Archer's attack:", Archer.attack)
    print ("Here is the Slime's Attack:", Slime.attack)

    def compare_archerattack_slime():
        if Archer.attack > Slime.attack:
            print ("You have won in this stat, good luck in the next.")
            slime_listy.append("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerattack_slime()

    input ("---")

    print ("Here is your Archer's health:", Archer.health)
    print ("Here is the Slime's health:", Slime.health)

    def compare_archerhealth_slime():
        if Archer.speed > Slime.speed:
            print ("You have won in this stat, good luck in the next.")
            slime_listy.append ("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerhealth_slime()

    input ("---")

    print ("Here is your Archer's speed:", Archer.speed)
    print ("Here is the Slime's speed:", Slime.speed)

    def compare_archerspeed_slime():
        if Archer.speed > Slime.speed:
            print ("You have won in this stat, good luck in the next.")
            slime_listy.append ("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerspeed_slime()

    def slime_winny():
        if len(slime_listy) > 1:
            print ("You have beaten the Slime, good luck on your next boss")
        else:
            print ("You have died. Start Over by rerunning the code.")
    slime_winny()
vs_slime()

def vs_Gob():

    print ("You have found a Goblin. Good luck")
    
    input ("---")
    
    print ("Here is The Goblin's attack", Goblin.attack)
    print ("Here are your Archers attack", Archer.attack)
    
    goblin_list = []
    
    def compare_goblin_attack():
        if Archer.attack > Goblin.attack:
            print ("You have won this stat, move on to the next.")
            goblin_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_goblin_attack()
    
    input ("---")
    
    print ("Here is The Goblin's health", Goblin.health)
    print ("Here are your Archers health", Archer.health) 
    
    def compare_goblin_health():
        if Archer.health > Goblin.health:
            print ("You have won this stat, move on to the next.")
            goblin_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_goblin_health()
    
    input ("---")
    
    print ("Here is The Goblin's speed", Goblin.speed)
    print ("Here are your Archers speed", Archer.speed) 
    
    
    def compare_goblin_speed():
        if Archer.speed > Goblin.speed:
            print ("You have won this stat, move on to the next.")
            goblin_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_goblin_speed()
    
    input ("---")
    
    def goblin_winny():
        if len(goblin_list) > 1:
            print ("You have beaten the Goblin, good luck on your next boss")
        else:
            print ("You have died. Start Over by rerunning the code.")
    goblin_winny()



def vs_Skele():

    print ("You have found a Skeleton. Good luck")

    input ("---")

    print ("Here is The Skeleton's attack", Skeleton.attack)
    print ("Here are your Archers attack", Archer.attack)

    skele_list = []

    def compare_skele_attack():
        if Archer.attack > Skeleton.attack:
            print ("You have won this stat, move on to the next.")
            skele_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_skele_attack()

    input ("---")

    print ("Here is The Skeleton's health", Skeleton.health)
    print ("Here are your Archers health", Archer.health) 

    def compare_skele_health():
        if Archer.health > Skeleton.health:
            print ("You have won this stat, move on to the next.")
            skele_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_skele_health()

    input ("---")

    print ("Here is The Skeleton's speed", Skeleton.speed)
    print ("Here are your Archers speed", Archer.speed) 


    def compare_skele_speed():
        if Archer.speed > Skeleton.speed:
            print ("You have won this stat, your fate will be revealed.")
            skele_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed")
    compare_skele_speed()

    input ("---")

    def skele_winny():
        if len(skele_list) > 1:
            print ("You have beaten the skeleton, good luck on your next boss")
        else:
            print ("You have died. Try Again by rerunning the code.")
    skele_winny()
