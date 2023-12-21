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
    start = 1
    end = 5
    values = list(range(start,end))
    item_drop = random.choice(values)
    if item_drop == (1):
        print ("Congrats a item has dropped")
        while item_drop == (1):
            start = 1
            end = 5
            values = list(range(start,end))
            item_choice = random.choice(values)
            if item_choice == (1):
                print ("Your prize is a shield")
            elif item_choice == (2):
                print ("Your prize is a chestplate")
            if item_choice == (3):
                print ("Your prize is a pair of boots")
            elif item_choice == (4):
                print ("Your prize is a cloak")
            break

def itemplacer():