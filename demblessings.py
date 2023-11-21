import random
import json
import os

class Blessings():
    class Hercules():
        def Defensebuff():
            start = 20
            end = 25
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            print ("This charm is imbued with the vitality of Hercules and it provides a boost of",randomnum, "to your health, use it well")
            Herculesbuff = randomnum
        Defensebuff()

    class Hermes():
        def Speedbuff():
            start = 20
            end = 25
            values = list(range(start,end))
            randomnum = (random.choice(values))
            print ("This charm is imbued with the agility of Hermes and it provides a boost of",randomnum, "to your speed, use it wisely")
            Hermesbuff = randomnum
        Speedbuff()

    class Artemis():
        def Attackbuff():
            start = 20
            end = 25 
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            print ("This charm is imbued with the agility of Hermes and it provides a boost of",randomnum, "to your speed, use it wisely")
            Artemisbuff = randomnum
        Attackbuff()


Blessings()



        