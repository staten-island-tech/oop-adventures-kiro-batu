import random

class troops:
    def __init__ (self, name, attack, speed, health):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.health = health

#for the archers
<<<<<<< HEAD
start = 10
end = 50 
values = list(range(start,end))
archer_randomattack= random.choice(values)

start = 1
end = 40
values = list(range(start,end))
archer_randomspeed= random.choice(values)

start = 1
=======
start = 15
end = 30
values = list(range(start,end))
archer_randomattack= random.choice(values)

start = 15
end = 30
values = list(range(start,end))
archer_randomspeed= random.choice(values)

start = 15
>>>>>>> Troops
end = 30
values = list(range(start,end))
archer_randomhealth= random.choice(values)

#for the infantry
start = 15
<<<<<<< HEAD
end = 50
=======
end = 35
>>>>>>> Troops
values = list(range(start,end))
infantry_randomattack= random.choice(values)

start = 5
end = 40
values = list(range(start,end))
infantry_randomspeed= random.choice(values)

start = 10
<<<<<<< HEAD
end = 40
=======
end = 35
>>>>>>> Troops
values = list(range(start,end))
infantry_randomhealth= random.choice(values)

#for the cavalry
<<<<<<< HEAD
start = 1
=======
start = 10
>>>>>>> Troops
end = 40 
values = list(range(start,end))
randomattack= random.choice(values)
cavalry_randomattack = random.choice(values)

<<<<<<< HEAD
start = 15
end = 60
=======
start = 10
end = 40
>>>>>>> Troops
values = list(range(start,end))
randomspeed= random.choice(values)
cavalry_randomspeed = random.choice(values)

<<<<<<< HEAD
start = 1
end = 50
=======
start = 15
end = 40
>>>>>>> Troops
values = list(range(start,end))
randomhealth= random.choice(values)
cavalry_randomhealth = random.choice(values)

Archer = troops ('Archers', archer_randomattack, archer_randomspeed, archer_randomhealth)
Infantry = troops ('Infantry', infantry_randomattack, infantry_randomspeed, infantry_randomhealth)
<<<<<<< HEAD
Cavalry = troops ('Cavalry', cavalry_randomattack, cavalry_randomspeed, cavalry_randomhealth)
=======
Cavalry = troops ('Cavalry', cavalry_randomattack,cavalry_randomspeed,cavalry_randomhealth)

print (Archer.attack, Infantry.speed, Cavalry.health)

>>>>>>> Troops

