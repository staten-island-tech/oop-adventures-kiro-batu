print ("You have encountered some Enemies on your way. These Enemies only get bigger and harder to defeat. We will start off easy.")

class Enemies ():
    class Slimes():
        def SlimeAppear():
            print ("OH NO YOU FOUND A SLIME")
            print ("Here are his stats")
            slimehealth = 10
            slimeattack = 5
            slimespeed = 0
            print ("Health: 10")
            print ("Attack: 5")
            print ("Speed: This enemy has no speed as it is too slow")
        SlimeAppear()

    class Zombies():
        def ZombieAppear():
            print ("OH NO YOU FOUND A ZOMBIE")
            print ("Here are his stats")
            zombiehealth = 0
            zombieattack = 10
            zombiespeed=5
            print ("Health: This enemy has no health as it is dying")
            print ("Attack: 10")
            print ("Speed: 5")
        ZombieAppear()