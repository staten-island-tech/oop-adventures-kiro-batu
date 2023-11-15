import random

def ArcherAttack():
    start = 10
    end = 50 
    values = list(range(start,end))
    randomattack= random.choice(values)
    print ("Your Archer Attack is:", randomattack)
ArcherAttack()
