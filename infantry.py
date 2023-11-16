import random

print ("When you run this code, you will get a random attack for your Infantry (15-50), random speed for your Infantry (5-40), and random health for your Infantry (10-40)")

class Infantry ():

    def InfantryAttack():
        start = 15
        end = 50 
        values = list(range(start,end))
        randomattack= random.choice(values)
        print ("Your Infantry Attack is:", randomattack)
    InfantryAttack()


    def InfantrySpeed():
        start = 5
        end = 40
        values = list(range(start,end))
        randomspeed= random.choice(values)
        print ("Your Infantry Speed is:", randomspeed)
    InfantrySpeed()


    def InfantryHealth():
        start = 10
        end = 40
        values = list(range(start,end))
        randomhealth= random.choice(values)
        print ("Your Infantry Health is:", randomhealth)
    InfantryHealth()

Infantry()