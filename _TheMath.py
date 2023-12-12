from troops import Archer
from enemies import Slime
from enemies import Skeleton

print ("Dont worry about the number above")

def Slime():

    print ("You have found a Slime. Good luck")
    
    input ("---")
    
    print ("Here is The Slime's attack", Slime.attack)
    print ("Here are your Archers attack", Archer.attack)
    
    slime_list = []
    
    def compare_slime_attack():
        if Archer.attack > Slime.attack:
            print ("You have won this stat, move on to the next.")
            slime_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_slime_attack()
    
    input ("---")
    
    print ("Here is The Slime's health", Slime.health)
    print ("Here are your Archers health", Archer.health) 
    
    def compare_slime_health():
        if Archer.health > Slime.health:
            print ("You have won this stat, move on to the next.")
            slime_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_slime_health()
    
    input ("---")
    
    print ("Here is The Slime's speed", Slime.speed)
    print ("Here are your Archers speed", Archer.speed) 
    
    
    def compare_slime_speed():
        if Archer.speed > Slime.speed:
            print ("You have won this stat, move on to the next.")
            slime_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_slime_speed()
    
    input ("---")
    
    def slime_winny():
        if len(slime_list) > 1:
            print ("You have beaten the Slime, good luck on your next boss")
        else:
            print ("You have died. Start Over by rerunning the code.")
    slime_winny()
Slime()


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