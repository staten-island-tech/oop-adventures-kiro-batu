import random 

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
    itemtype = ("Boots")
    def speed():
        start = 5
        end = 15
        values = list(range(start, end)) 
        randomnum = (random.choice(values))
        print ("This pair of boots provides a boost of",randomnum, "to your health")
    speed()
Boots(): 

