import random

class troops:
    def __init__ (self, name, attack, speed, health):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.health = health

    def balancer(self):
        if self.attack < (0):
            self.attack == (0)
        if self.speed < (0):
            self.speed == (0)
        if self.health < (0):
            self.health == (0)
    balancer()


     

class Archerrandom():
    start = 10
    end = 15
    values = list(range(start,end))
    global archer_randomattack
    archer_randomattack= random.choice(values)

    start = 5
    end = 15
    values = list(range(start,end))
    global archer_randomspeed
    archer_randomspeed= random.choice(values)

    start = 5
    end = 10
    values = list(range(start,end))
    global archer_randomhealth
    archer_randomhealth= random.choice(values)

class Infantryrandom():
    start = 10
    end = 15
    values = list(range(start,end))
    global infantry_randomattack
    infantry_randomattack= random.choice(values)

    start = 5
    end = 10
    values = list(range(start,end))
    global infantry_randomspeed
    infantry_randomspeed= random.choice(values)

    start = 5
    end = 15
    values = list(range(start,end))
    global infantry_randomhealth
    infantry_randomhealth= random.choice(values)

class Cavalryrandom():
    start = 5
    end = 10
    values = list(range(start,end))
    randomattack= random.choice(values)
    global cavalry_randomattack
    cavalry_randomattack = random.choice(values)

    start = 10
    end = 15
    values = list(range(start,end))
    randomspeed= random.choice(values)
    global cavalry_randomspeed
    cavalry_randomspeed = random.choice(values)

    start = 5
    end = 15
    
    values = list(range(start,end))
    randomhealth= random.choice(values)
    global cavalry_randomhealth
    cavalry_randomhealth = random.choice(values)

Archer = troops ('Archers', archer_randomattack, archer_randomspeed, archer_randomhealth)
Infantry = troops ('Infantry', infantry_randomattack, infantry_randomspeed, infantry_randomhealth)
Cavalry = troops ('Cavalry', cavalry_randomattack, cavalry_randomspeed, cavalry_randomhealth)









