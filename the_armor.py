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

print (Cloak)

trooplisty = ['Cavalry']


##shield buff
def archer_shield():
    Archer.health += Shield.health
    Archer.speed -= Shield.speed
def infantry_shield():
    Infantry.health += Shield.health
    Infantry.speed -= Shield.speed
def cavalry_shield():
    Cavalry.health += Shield.health
    Cavalry.speed -= Shield.speed

##boots buff
def archer_boots():
    Archer.speed += Shield.speed
def infantry_boots():
    Infantry.speed += Shield.speed
def cavalry_boots():
    Cavalry.speed += Shield.speed

##chestplate buff
def archer_chestplate():
    Archer.health += Chestplate.health
    Archer.speed -= Chestplate.speed
def infantry_chestplate():
    Infantry.health += Chestplate.health
    Infantry.speed -= Chestplate.speed
def cavalry_chestplate():
    Cavalry.health += Chestplate.health
    Cavalry.speed -= Chestplate.speed

## cloak buff
def archer_cloak():
    Archer.health += Cloak.health
    Archer.speed -= Cloak.speed
def infantry_cloak():
    Infantry.health += Cloak.health
    Infantry.speed += Cloak.speed
def cavalry_cloak():
    Cavalry.health += Cloak.health
    Cavalry.speed += Cloak.speed


def itemdrop():
    trooplist = ["Cavalry", "Archer", "Infantry" ]
    
    start = 1
    end = 2
    values = list(range(start,end))
    item_drop = random.choice(values)
    if item_drop == (1):
        print ("- Congrats a item has dropped")
        while item_drop == (1):
            start = 1
            end = 5
            values = list(range(start,end))
            item_choice = random.choice(values)
            if item_choice == (1):
                print ("- Your prize is a shield")
                print ("This shield can provide a buff of", ShieldHealth, "to any of your troops current Health")
                print ("Yet this shield also decreases the speed of your troops by", ShieldSpeed)
            elif item_choice == (2):
                print ("- Your prize is a chestplate")
                print ("---")
                print ("This chestplate can increase the health of your troops by", ChestplateHealth)
                print ("Although, this chestplate also decreases the speed of your troops by", ChestplateSpeed)
            if item_choice == (3):
                print ("- Your prize is a pair of boots")
                print ("These pair of boots provide a buff to the speed of your troops", BootSpeed)
            elif item_choice == (4):
                print ("- Your prize is a cloak")
                print ("This cloak can provide a buff of", CloakHealth, "to any of your troops current Health")
                print ("Moreover this cloak also increase the speed of your troops by", CloakSpeed)
            break
        
    troopinput = input("Select a troop type to award you're item to: ")
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
itemdrop()
