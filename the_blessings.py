import random
from troops import Archer, Infantry, Cavalry

class blessing:
    def __init__(self, name, defense, speed, attack):
        self.name = name
        self.defense = defense
        self.speed = speed
        self.attack = attack


##hercules
start = 20
end = 25
values = list(range(start, end)) 
randomnum = (random.choice(values))
Herculesbuff = randomnum
##print ("This charm is imbued with the vitality of Hercules and it provides a boost of",Herculesbuff, "to your health, use it well")

Hercules = blessing('Hercules', Herculesbuff, 0, 0)

##hermes
start = 20
end = 25
values = list(range(start,end))
randomnum = (random.choice(values))
Hermesbuff = randomnum
##print ("This charm is imbued with the agility of Hermes and it provides a boost of",Hermesbuff, "to your speed, use it wisely")
        
Hermes = blessing("Hermes", 0, Hermesbuff, 0 )

##artemis
start = 20
end = 25 
values = list(range(start, end)) 
randomnum = (random.choice(values))
Artemisbuff = randomnum
##print ("This charm is imbued with the agility of Hermes and it provides a boost of",Artemisbuff, "to your speed, use it wisely")

Artemis = blessing("Artemis", 0, 0, Artemisbuff)


def archer_artemis():
    Archer.attack += Artemis.attack
    print("Your archer's attack stat has been updated to", Archer.attack)
def infantry_artemis():
    Infantry.attack += Artemis.attack
    print("Your infantry's attack stat has been updated to", Infantry.attack)
def cavalry_artemis():
    Cavalry.attack += Artemis.attack
    print("Your cavalry's attack stat has been updated to", Cavalry.attack)

##speed Buff
def archer_hermes():
    Archer.speed += Hermes.speed
    print("Your archer's speed stat has been updated to", Archer.speed)
def infantry_hermes():
    Infantry.speed += Hermes.speed
    print("Your infantry's attack stat has been updated to", Infantry.speed)
def cavalry_hermes():
    Cavalry.speed += Hermes.speed
    print("Your cavalry's attack stat has been updated to", Cavalry.speed)

##health Buff
def archer_hercules():
    Archer.health += Hercules.defense
    print("Your archer's health stat has been updated to", Archer.health)
def infantry_hercules():
    Infantry.health += Hercules.defense
    print("Your infantry's health stat has been updated to", Infantry.health)
def cavalry_hercules():
    Cavalry.attack += Hercules.defense
    print("Your cavalry's health stat has been updated to", Cavalry.health)

<<<<<<< HEAD
trooplist = ["Cavalry", "Archer", "Infantry" ]



def blessingdrop():
    start = 1
<<<<<<< HEAD
    end = 5
=======
    end = 9
>>>>>>> Numbers
    values = list(range(start,end))
    global item_drop
    item_drop = random.choice(values)

    start = 1
    end = 4
    values = list(range(start,end))
    global item_choice
    item_choice = random.choice(values)

    if item_drop == (1): 
        print ("---")
        print ("Congrats a mystical blessing has fallen")
        while item_drop == (1):

            if item_choice == (1):
                input ("Artemis has offered to bless one of your troops: ")
                print ("---")
                print ("This charm channels her legendary prowess and provides a buff of", Artemisbuff, "to any of your troops current Attack")
            elif item_choice == (2):
                input ("Hermes has offered to bless one of your troops: ")
                print ("---")
                print ("This charm channel his miraculous agility and buff the Speed of your troops by", Hermesbuff)
            if item_choice == (3):
                input ("Hercules has offered to bless one of your troops: ")
                print ("---")
                print ("This charm channel his mighty strength and provides a buff of", Herculesbuff, "to the Attack of your troops")
            break

        if item_drop == (1):
            print ("---")
            input("Before making a decision the stats of all your troops will be shown: ")
            print ("---")
            print ("- Cavalry: Attack: ", Cavalry.attack)
            print ("- Cavalry: Speed: ", Cavalry.speed )
            print ("- Cavalry: Health: ", Cavalry.health)
            print ("---")
            print ("- Archer: Attack: ", Archer.attack)
            print ("- Archer: Speed: ", Archer.speed )
            print ("- Archer: Health: ", Archer.health)
            print ("---")
            print ("- Infantry: Attack: ", Infantry.attack)
            print ("- Infantry: Speed: ", Infantry.speed )
            print ("- Infantry: Health: ", Infantry.health)
            print ("---")


def the_choice():
    while item_drop == (1):
            troopinputbd = input("Select a troop type to award you're item to: ")
            print("---")
            
            if troopinputbd == ("Cavalry"):
                input ("You have picked the cavalry, its updated stats will be shown")
                print ("---")
                if item_choice == (1):
                    cavalry_artemis()
                    print ("---")
                    print ("- Attack: ", Cavalry.attack)
                    print ("- Speed: ", Cavalry.speed )
                    print ("- Health: ", Cavalry.health)
                elif item_choice == (2):
                    cavalry_hermes()
                    print ("---")
                    print ("- Attack: ", Cavalry.attack)
                    print ("- Speed: ", Cavalry.speed )
                    print ("- Health: ", Cavalry.health)
                elif item_choice == (3):
                    cavalry_hercules()
                    print ("---")
                    print ("- Attack: ", Cavalry.attack)
                    print ("- Speed: ", Cavalry.speed )
                    print ("- Health: ", Cavalry.health)
                break

            if troopinputbd == ("Archer"):
                input ("You have picked the archer, its updated stats will be shown")
                print ("---")
                if item_choice == (1):
                    archer_artemis()
                    print ("---")
                    print ("- Attack: ", Archer.attack)
                    print ("- Speed: ", Archer.speed )
                    print ("- Health: ", Archer.health)
                elif item_choice == (2):
                    archer_hermes()
                    print ("---")
                    print ("- Attack: ", Archer.attack)
                    print ("- Speed: ", Archer.speed )
                    print ("- Health: ", Archer.health)
                elif item_choice == (3):
                    archer_hercules()
                    print ("---")
                    print ("- Attack: ", Archer.attack)
                    print ("- Speed: ", Archer.speed )
                    print ("- Health: ", Archer.health)
                break
       
            if troopinputbd == ("Infantry"):
                input ("You have picked the infantry, its updated stats will be shown")
                print ("---")
                if item_choice == (1):
                    infantry_artemis()
                    print ("---")
                    print ("- Attack: ", Infantry.attack)
                    print ("- Speed: ", Infantry.speed )
                    print ("- Health: ", Infantry.health)
                elif item_choice == (2):
                    infantry_hermes()
                    print ("---")
                    print ("- Attack: ", Infantry.attack)
                    print ("- Speed: ", Infantry.speed )
                    print ("- Health: ", Infantry.health)
                elif item_choice == (3):
                    infantry_hercules()
                    print ("---")
                    print ("- Attack: ", Infantry.attack)
                    print ("- Speed: ", Infantry.speed )
                    print ("- Health: ", Infantry.health)
                break
            if not troopinputbd in trooplist:
                print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
                return the_choice()

=======
>>>>>>> Blessings
