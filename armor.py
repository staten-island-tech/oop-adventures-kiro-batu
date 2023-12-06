import random 

<<<<<<< HEAD
class item():
    class Shield():
        itemtype = ("Armor")
        def health():
            start = 5
            end = 15
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            ShieldHealth = randomnum
            print ("This shield provides a boost of",ShieldHealth, "to your health")
        def speed ():
            start = 5
            end = 15
            values = list(range(start, end))
            randomnum = (random.choice(values))
            ShieldSpeed = randomnum
            print ("Yet this shield also makes you slower by", ShieldSpeed )
    

    class Boots():
        itemtype = ("Armor")
        def speed():
            start = 5
            end = 15
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            BootsSpeed=randomnum
            print ("This pair of boots provides a boost of",BootsSpeed, "to your speed")
 

    class Chestplate():
        itemtype = ("Armor")
        def health():
            start = 10
            end = 20
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            ChestplateHealth = randomnum
            print ("This chestplate provides a boost of",ChestplateHealth, "to your health")
        def speed ():
            start = 5
            end = 15
            values = list(range(start, end))
            randomnum = (random.choice(values))
            ChestplateSpeed = randomnum
            print ("Yet this chestplate also makes you slower by", ChestplateSpeed )


    class Cloak():
        itemtype = ("Armor")
        def health():
            start = 5
            end = 10
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            CloakHealth = randomnum
            print ("This cloack provides a boost of", CloakHealth, "to your health")
        def speed ():
            start = 10
            end = 20
            values = list(range(start, end))
            randomnum = (random.choice(values))
            CloakSpeed = randomnum
            print ("This cloak also makes you faster by", CloakSpeed )
   

=======
class drops:
    def __init__(self, name, drop, health, speed):
        self.name = name
        self.drop = drop
        self.health =  health
        self.speed =  speed

##shield
Shieldtype = ("Item")
  
start = 5
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
>>>>>>> items

