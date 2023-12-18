from troops import Archer
from enemies import Slime

def vs_slime():
    print ("Dont worry about the number above")
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
        if Slime.health > Archer.health:
            print ("You have won in this stat, good luck in the next.")
            slime_listy.append ("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerhealth_slime()

    input ("---")

    print ("Here is your Archer's speed:", Archer.speed)
    print ("Here is the Slime's speed:", Slime.speed)

    def compare_archerspeed_slime():
        if Slime.speed > Archer.speed:
            print ("You have won in this stat, good luck in the next.")
            slime_listy.append ("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerspeed_slime

    print (slime_listy)
vs_slime()