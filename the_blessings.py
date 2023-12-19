import random

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

