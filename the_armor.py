import random 
from troops import Archer, Infantry, Cavalry

class drops:
    def __init__(self, name, drop, health, speed):
        self.name = name
        self.drop = drop
        self.health =  health
        self.speed =  speed

##shield
Shieldtype = ("Item")
  
start = 10
end = 15
values = list(range(start, end)) 
randomnum = (random.choice(values))
ShieldHealth = randomnum

start = 5
end = 15
values = list(range(start, end))
randomnum = (random.choice(values))
ShieldSpeed = randomnum

Shield = drops ('Shield',Shieldtype, ShieldHealth, ShieldSpeed)

##boots
Boottype = ("Armor")

BootHealth = ("0")

start = 5
end = 15
values = list(range(start, end)) 
randomnum = (random.choice(values))
BootSpeed= randomnum

Boots = drops ('Boots', Boottype, BootHealth, BootSpeed )

##chestplate
Chestplatetype = ("Armor")
     
start = 10
end = 20
values = list(range(start, end)) 
randomnum = (random.choice(values))
ChestplateHealth = randomnum

start = 5
end = 15
values = list(range(start, end))
randomnum = (random.choice(values))
ChestplateSpeed = randomnum

Chestplate = drops ("Chestplate", Chestplatetype, ChestplateHealth, ChestplateSpeed)

##cloak

Cloaktype = ("Armor")

start = 5
end = 10
values = list(range(start, end)) 
randomnum = (random.choice(values))
CloakHealth = randomnum

start = 10
end = 20
values = list(range(start, end))
randomnum = (random.choice(values))
CloakSpeed = randomnum

Cloak = drops ("Cloak", Cloaktype, CloakHealth, CloakSpeed )





##shield buff
def archer_shield():
    Archer.health += Shield.health
    Archer.speed -= Shield.speed
    print("Your archer's health stat has been updated to", Archer.health)
    print("Your archer's speed stat has been updated to", Archer.speed)
def infantry_shield():
    Infantry.health += Shield.health
    Infantry.speed -= Shield.speed
    print("Your infantry's health stat has been updated to", Infantry.health)
    print("Your infantry's speed stat has been updated to", Infantry.speed)
def cavalry_shield():
    Cavalry.health += Shield.health
    Cavalry.speed -= Shield.speed
    print("Your cavalry's health stat has been updated to", Cavalry.health)
    print("Your cavalry's speed stat has been updated to", Cavalry.speed)

##boots buff
def archer_boots():
    Archer.speed += Shield.speed
    print("Your Archer's speed has been updated to", Archer.speed)
def infantry_boots():
    Infantry.speed += Shield.speed
    print("Your infantry's speed has been updated to", Infantry.speed)
def cavalry_boots():
    Cavalry.speed += Shield.speed
    print("Your cavalry's speed has been updated to", Cavalry.speed)

##chestplate buff
def archer_chestplate():
    Archer.health += Chestplate.health
    Archer.speed -= Chestplate.speed
    print("Your archer's health stat has been updated to", Archer.health)
    print("Your archer's speed stat has been updated to", Archer.speed)
def infantry_chestplate():
    Infantry.health += Chestplate.health
    Infantry.speed -= Chestplate.speed
    print("Your infantry's health stat has been updated to", Infantry.health)
    print("Your infantry's speed stat has been updated to", Infantry.speed)
def cavalry_chestplate():
    Cavalry.health += Chestplate.health
    Cavalry.speed -= Chestplate.speed
    print("Your cavalry's health stat has been updated to", Cavalry.health)
    print("Your cavalry's speed stat has been updated to", Cavalry.speed)

## cloak buff
def archer_cloak():
    Archer.health += Cloak.health
    Archer.speed += Cloak.speed
    print("Your archer's health stat has been updated to", Archer.health)
    print("Your archer's speed stat has been updated to", Archer.speed)
def infantry_cloak():
    Infantry.health += Cloak.health
    Infantry.speed += Cloak.speed
    print("Your infantry's health stat has been updated to", Infantry.health)
    print("Your infantry's speed stat has been updated to", Infantry.speed)
def cavalry_cloak():
    Cavalry.health += Cloak.health
    Cavalry.speed += Cloak.speed
    print("Your cavalry's health stat has been updated to", Cavalry.health)
    print("Your cavalry's speed stat has been updated to", Cavalry.speed)


def itemdrop():
    trooplist = ["Cavalry", "Archer", "Infantry" ]
    
    start = 1
    end = 6
    values = list(range(start,end))
    item_drop = random.choice(values)
    if item_drop == (1): 
        print ("---")
        print ("Congrats an item has dropped")
        while item_drop == (1):
            start = 1
            end = 5
            values = list(range(start,end))
            item_choice = random.choice(values)
            if item_choice == (1):
                input ("Your prize is a shield")
                print ("---")
                print ("This shield can provide a buff of", ShieldHealth, "to any of your troops current Health")
                print ("Yet this shield also decreases the speed of your troops by", ShieldSpeed)
            elif item_choice == (2):
                input ("Your prize is a chestplate")
                print ("---")
                print ("This chestplate can increase the health of your troops by", ChestplateHealth)
                print ("Although, this chestplate also decreases the speed of your troops by", ChestplateSpeed)
            if item_choice == (3):
                input ("Your prize is a pair of boots")
                print ("---")
                print ("These pair of boots provide a buff of", BootSpeed, "to the speed of your troops")
            elif item_choice == (4):
                input ("Your prize is a cloak")
                print ("---")
                print ("This cloak can provide a buff of", CloakHealth, "to any of your troops current Health")
                print ("Moreover this cloak also increase the speed of your troops by", CloakSpeed)
            break
        
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

    troopinput = input("Select a troop type to award you're item to: ")
    print("---")

    while troopinput == ("Cavalry"):
        input ("You have picked the cavalry, its updated stats will be shown")
        print ("---")
        if item_choice == (1):
            cavalry_shield()
            print ("---")
            print ("- Attack: ", Cavalry.attack)
            print ("- Speed: ", Cavalry.speed )
            print ("- Health: ", Cavalry.health)
        elif item_choice == (2):
            cavalry_chestplate()
            print ("---")
            print ("- Attack: ", Cavalry.attack)
            print ("- Speed: ", Cavalry.speed )
            print ("- Health: ", Cavalry.health)
        if item_choice == (3):
            cavalry_boots()
            print ("---")
            print ("- Attack: ", Cavalry.attack)
            print ("- Speed: ", Cavalry.speed )
            print ("- Health: ", Cavalry.health)
        elif item_choice == (4):
            cavalry_cloak()
            print ("---")
            print ("- Attack: ", Cavalry.attack)
            print ("- Speed: ", Cavalry.speed )
            print ("- Health: ", Cavalry.health)
        break

    
    while troopinput == ("Archer"):
        input ("You have picked the archer, its updated stats will be shown")
        print ("---")
        if item_choice == (1):
            archer_shield()
            print ("---")
            print ("- Attack: ", Archer.attack)
            print ("- Speed: ", Archer.speed )
            print ("- Health: ", Archer.health)
        elif item_choice == (2):
            archer_chestplate()
            print ("---")
            print ("- Attack: ", Archer.attack)
            print ("- Speed: ", Archer.speed )
            print ("- Health: ", Archer.health)
        if item_choice == (3):
            archer_boots()
            print ("---")
            print ("- Attack: ", Archer.attack)
            print ("- Speed: ", Archer.speed )
            print ("- Health: ", Archer.health)
        elif item_choice == (4):
            archer_cloak()
            print ("---")
            print ("- Attack: ", Archer.attack)
            print ("- Speed: ", Archer.speed )
            print ("- Health: ", Archer.health)
        break

    while troopinput == ("Infantry"):
        input ("You have picked the infantry, its updated stats will be shown")
        print ("---")
        if item_choice == (1):
            infantry_shield()
            print ("---")
            print ("- Attack: ", Infantry.attack)
            print ("- Speed: ", Infantry.speed )
            print ("- Health: ", Infantry.health)
        elif item_choice == (2):
            infantry_chestplate()
            print ("---")
            print ("- Attack: ", Infantry.attack)
            print ("- Speed: ", Infantry.speed )
            print ("- Health: ", Infantry.health)
        if item_choice == (3):
            infantry_boots()
            print ("---")
            print ("- Attack: ", Infantry.attack)
            print ("- Speed: ", Infantry.speed )
            print ("- Health: ", Infantry.health)
        elif item_choice == (4):
            infantry_cloak()
            print ("---")
            print ("- Attack: ", Infantry.attack)
            print ("- Speed: ", Infantry.speed )
            print ("- Health: ", Infantry.health)
        break
itemdrop()
