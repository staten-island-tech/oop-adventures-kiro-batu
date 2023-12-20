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

##attack buff
def archer_artemis():
    Archer.attack += Artemis.attack
    print(Archer.attack)
def infantry_artemis():
    Infantry.attack += Artemis.attack
    print(Infantry.attack)
def cavalry_artemis():
    Cavalry.attack += Artemis.attack
    print(Cavalry.attack)

##speed Buff
def archer_hermes():
    Archer.speed += Hermes.speed
    print(Archer.speed)
def infantry_hermes():
    Infantry.speed += Hermes.speed
    print(Infantry.speed)
def cavalry_hermes():
    Cavalry.speed += Hermes.speed
    print(Cavalry.speed)

##health Buff
def archer_hercules():
    Archer.health += Hercules.defense
    print(Archer.health)
def infantry_hercules():
    Infantry.health += Artemis.defense
    print(Infantry.health)
def cavalry_hercules():
    Cavalry.attack += Artemis.defense
    print(Cavalry.health)

