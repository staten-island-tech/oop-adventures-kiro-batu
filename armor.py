import random 


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
    Shield()

    class Boots():
        itemtype = ("Armor")
        def speed():
            start = 5
            end = 15
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            BootsSpeed=randomnum
            print ("This pair of boots provides a boost of",BootsSpeed, "to your speed")
    Boots()

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
    Chestplate()

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
    Cloak()
item()

