from troops import Archer
from enemies import Skeleton


print ("Dont worry about the number above")

def Goblin():

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



def Skeleton():

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
            print ("You have won this stat, move on to the next.")
            skele_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_skele_speed()

    input ("---")

    def skele_winny():
        if len(skele_list) > 1:
            print ("You have beaten the skeleton, good luck on your next boss")
        else:
            print ("You have died. Try Again by rerunning the code.")
Skeleton()