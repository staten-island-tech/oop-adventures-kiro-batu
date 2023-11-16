import random

print ("When you run this code, you will get a random attack for your Cavalry (1-40), random speed for your Cavalry (15-60), and random health for your Cavalry (1-50)")

class Cavalry ():

    def CavalryAttack():
        start = 1
        end = 40 
        values = list(range(start,end))
        randomattack= random.choice(values)
        print ("Your Cavalry Attack is:", randomattack)
    CavalryAttack()


    def CavalrySpeed():
        start = 15
        end = 60
        values = list(range(start,end))
        randomspeed= random.choice(values)
        print ("Your Cavalry Speed is:", randomspeed)
    CavalrySpeed()


    def CavalryHealth():
        start = 1
        end = 50
        values = list(range(start,end))
        randomhealth= random.choice(values)
        print ("Your Cavalry Health is:", randomhealth)
    CavalryHealth()
Cavalry()