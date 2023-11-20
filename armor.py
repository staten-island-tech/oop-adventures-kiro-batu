import random 


class item():
    class Shield():
        itemtype = ("Armor")
        def health():
            start = 5
            end = 15
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            print ("This shield provides a boost of",randomnum, "to your health")
        def speed ():
            start = 5
            end = 15
            values = list(range(start, end))
            randomnum = (random.choice(values))
            print ("Yet this shield also makes you slower by", randomnum )
        health()
        speed()
    Shield()

    class Boots():
        itemtype = ("Armor")
        def speed():
            start = 5
            end = 15
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            print ("This pair of boots provides a boost of",randomnum, "to your speed")
        speed()
    Boots()

    class Chestplate():
        itemtype = ("Armor")
        def health():
            start = 10
            end = 20
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            print ("This chestplate provides a boost of",randomnum, "to your health")
        def speed ():
            start = 5
            end = 15
            values = list(range(start, end))
            randomnum = (random.choice(values))
            print ("Yet this chestplate also makes you slower by", randomnum )
        health()
        speed()
    Chestplate()

    class Cloak():
        itemtype = ("Armor")
        def health():
            start = 5
            end = 10
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            print ("This cloack provides a boost of",randomnum, "to your health")
        def speed ():
            start = 10
            end = 20
            values = list(range(start, end))
            randomnum = (random.choice(values))
            print ("This cloak also makes you faster by", randomnum )
        health()
        speed()
    Cloak()
item()

