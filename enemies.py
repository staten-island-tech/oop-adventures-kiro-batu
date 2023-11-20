print ("You have encountered some Enemies on your way. These Enemies only get bigger and harder to defeat. We will start off easy.")

class Enemies ():
    class Slimes():
        def SlimeAppear():
            input ("OH NO YOU FOUND A SLIME: (Click enter to continue) ")
            print ("Here are his stats")
            slimehealth = 10
            slimeattack = 5
            slimespeed = 0
            print ("Health:",slimehealth)
            print ("Attack:",slimeattack)
            print ("Speed:",slimespeed)
        SlimeAppear()

    class Zombies():
        def ZombieAppear():
            input ("OH NO YOU FOUND A ZOMBIE: (Click enter to continue) ")
            print ("Here are his stats")
            zombiehealth = 0
            zombieattack = 10
            zombiespeed = 5
            print ("Health:",zombiehealth)
            print ("Attack:",zombieattack)
            print ("Speed:",zombiespeed)
        ZombieAppear()

    class Goblins():
        def GoblinAppear():
            input ("OH NO YOU FOUND A GOBLIN: (Click enter to continue) ")
            print ("Here are his stats")
            goblinhealth = 10
            goblinattack = 10
            goblinspeed = 10
            print ("Health: ",goblinhealth)
            print ("Attack: ",goblinattack)
            print ("Speed: ",goblinspeed)
        GoblinAppear()
    
    class Skeleton():
        def SkeletonAppear():
            input ("OH NO YOU FOUND A SKELETON: (Click enter to continue) ")
            print ("Here are his stats")
            skeletonhealth = 10
            skeletonattack = 7
            skeletonspeed = 15
            print ("Health: ",skeletonhealth)
            print ("Attack: ",skeletonattack)
            print ("Speed: ",skeletonspeed)
        SkeletonAppear()
    
    class Minotaur():
        def MinotaurAppear():
            input ("Now this will be your first real test: (Click enter to continue) ")
            print ("OH NO YOU FOUND A MINOTAUR")
            print ("Here are his stats")
            minotaurhealth = 20
            minotaurattack = 20
            minotaurspeed = 20
            print ("Health: ",minotaurhealth)
            print ("Attack: ",minotaurattack)
            print ("Speed: ",minotaurspeed)
        MinotaurAppear()

    class Cyclops():
        def CyclopsAppear():
            input ("OH NO YOU FOUND A CYCLOPS (Click enter to continue)")
            print ("Here are his stats")
            cyclopshealth = 25
            cyclopsattack = 25
            cyclopsspeed = 10
            print ("Health: ",cyclopshealth)
            print ("Attack: ",cyclopsattack)
            print ("Speed: ",cyclopsspeed)
        CyclopsAppear()

    
    class GiantSpider():
        def GiantSpiderAppear():
            input ("OH NO YOU FOUND A GIANT SPIDER (Click enter to continue)")
            print ("Here are his stats")
            giantspiderhealth = 20 
            giantspiderattack = 25
            giantspiderspeed = 30
            print ("Health: ",giantspiderhealth)
            print ("Attack: ",giantspiderattack)
            print ("Speed: ",giantspiderspeed)
        GiantSpiderAppear()

    class Yeti():
        def YetiAppear():
            input ("OH NO YOU FOUND A YETI (Click enter to continue)")
            print ("Here are his stats")
            yetihealth = 30
            yetiattack = 30
            yetispeed = 15
            print ("Health: ",yetihealth)
            print ("Attack: ",yetiattack)
            print ("Speed: ",yetispeed)
        YetiAppear() 

    class Hydra():
        def HydraAppear():
            input ("NOW THIS HYDRA IS THE FINAL BOSS, DEFEAT HIM TO WIN! (Click enter to continue)")
            print ("Here are his stats")
            hydrahealth = 40
            hydraattack = 40
            hydraspeed = 40
            print ("Health: ",hydrahealth)
            print ("Attack: ",hydraattack)
            print ("Speed: ",hydraspeed)
        HydraAppear()
Enemies()