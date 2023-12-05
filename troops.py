import random

class troops:
    def __init__ (self, name, attack, speed, health):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.health = health

start = 10
end = 50 
values = list(range(start,end))
archerrandomattack= random.choice(values)

start = 1
end = 40
values = list(range(start,end))
archerrandomspeed= random.choice(values)

start = 1
end = 30
values = list(range(start,end))
archerrandomhealth= random.choice(values)

Archer = troops ('Archers', archerrandomattack, archerrandomspeed, archerrandomhealth)

print (Archer.attack)