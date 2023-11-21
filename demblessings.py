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
            Herculesbuff = randomnum
            print ("This charm is imbued with the vitality of Hercules and it provides a boost of",Herculesbuff, "to your health, use it well")
            
        Defensebuff()

    class Hermes():
        def Speedbuff():
            start = 20
            end = 25
            values = list(range(start,end))
            randomnum = (random.choice(values))
            Hermesbuff = randomnum
            print ("This charm is imbued with the agility of Hermes and it provides a boost of",Hermesbuff, "to your speed, use it wisely")
            
        Speedbuff()

    class Artemis():
        def Attackbuff():
            start = 20
            end = 25 
            values = list(range(start, end)) 
            randomnum = (random.choice(values))
            Artemisbuff = randomnum
            print ("This charm is imbued with the agility of Hermes and it provides a boost of",Artemisbuff, "to your speed, use it wisely")
        Attackbuff()


Blessings()



        