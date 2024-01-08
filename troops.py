import random

class troops:
    def __init__ (self, name, attack, speed, health):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.health = health

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

if Archer.attack < (0):
    Archer.attack = 0
if Archer.health < (0):
    Archer.health = 0
if Archer.speed < (0):
    Archer.speed = 0

if Infantry.attack < (0):
    Infantry.attack = 0
if Infantry.health < (0):
    Infantry.health = 0
if Infantry.speed < (0):
    Infantry.speed = 0

if Cavalry.attack < (0):
    Cavalry.attack = 0
if Cavalry.health < (0):
    Cavalry.health = 0
if Cavalry.speed < (0):
    Cavalry.speed = 0






