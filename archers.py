import random


class archer ():
    def rundown():
        print ("When you run this code, you will get a random attack for your archer (10-50), random speed for your archer (1-40), and random health for your archer (1-30)")


    def ArcherAttack():
        start = 10
        end = 50 
        values = list(range(start,end))
        randomattack= random.choice(values)
        print ("Your Archer Attack is:", randomattack)
    


    def ArcherSpeed():
        start = 1
        end = 40
        values = list(range(start,end))
        randomspeed= random.choice(values)
        print ("Your Archer Speed is:", randomspeed)



    def ArcherHealth():
        start = 1
        end = 30
        values = list(range(start,end))
        randomhealth= random.choice(values)
        print ("Your Archer Health is:", randomhealth)
    
archer()