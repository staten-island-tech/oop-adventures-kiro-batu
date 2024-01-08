import random

class troops:
    def __init__ (self, name, attack, speed, health):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.health = health
        
        if self.attack < (0):
            self.attack = 0
        if self.speed < (0):
            self.speed = 0
        if self.health < (0):
            self.health = 0
     

#for the archers
start = 10
end = 15
values = list(range(start,end))
archer_randomattack= random.choice(values)

start = 5
end = 15
values = list(range(start,end))
archer_randomspeed= random.choice(values)

start = 5
end = 10
values = list(range(start,end))
archer_randomhealth= random.choice(values)

#for the infantry
start = 10
end = 15
values = list(range(start,end))
infantry_randomattack= random.choice(values)

start = 5
end = 10
values = list(range(start,end))
infantry_randomspeed= random.choice(values)

start = 5
end = 15
values = list(range(start,end))
infantry_randomhealth= random.choice(values)

#for the cavalry
start = 5
end = 10
values = list(range(start,end))
randomattack= random.choice(values)
cavalry_randomattack = random.choice(values)

start = 10
end = 15
values = list(range(start,end))
randomspeed= random.choice(values)
cavalry_randomspeed = random.choice(values)

start = 5
end = 15
values = list(range(start,end))
randomhealth= random.choice(values)
cavalry_randomhealth = random.choice(values)

Archer = troops ('Archers', archer_randomattack, archer_randomspeed, archer_randomhealth)
Infantry = troops ('Infantry', infantry_randomattack, infantry_randomspeed, infantry_randomhealth)
Cavalry = troops ('Cavalry', cavalry_randomattack, cavalry_randomspeed, cavalry_randomhealth)







