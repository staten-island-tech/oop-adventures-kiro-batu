import random


class Blessings():
    class Hercules():
        def Defensebuff():
            start = 20
            end = 25
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            print ("This charm imbued with the vitality of Hercules provides a boost of",randomnum, "to your health, use it well")
    class Hermes():
        def Speedbuff():
            start = 20