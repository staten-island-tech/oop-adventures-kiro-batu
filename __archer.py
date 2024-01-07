from troops import Archer
from enemies import Slime, Zombie, Goblin, Skeleton, Minotaur, Cyclops, GiantSpider, Yeti, Hydra, nelahWrM


slime_defeat = []
troopslime= ["Cavalry", "Archer", "Infantry" ]

def vs_slimea():
    
    print ("You have found a Slime, good luck in this battle")

    slime_listy = []

    input ("---")

    print ("Here is your Archer's attack:", Archer.attack)
    print ("Here is the Slime's Attack:", Slime.attack)

    def compare_archerattack_slime():
        if Archer.attack > Slime.attack:
            print ("You have won in this stat, good luck in the next.")
            slime_listy.append("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerattack_slime()

    input ("---")

    print ("Here is your Archer's health:", Archer.health)
    print ("Here is the Slime's health:", Slime.health)

    def compare_archerhealth_slime():
        if Archer.health > Slime.health:
            print ("You have won in this stat, good luck in the next.")
            slime_listy.append ("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerhealth_slime()

    input ("---")

    print ("Here is your Archer's speed:", Archer.speed)
    print ("Here is the Slime's speed:", Slime.speed)

    def compare_archerspeed_slime():
        if Archer.speed > Slime.speed:
            print ("You have won in this stat, good luck in the next.")
            slime_listy.append ("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerspeed_slime()

    input ("---")

    def slime_winny():
        if len(slime_listy) > 1:
            print ("You have beaten the SLIME, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    slime_winny()
   





def vs_zoma():

    print ("You have found a Zombie, good luck in this battle")

    zom_listy = []

    input ("---")

    print ("Here is your Archer's attack:", Archer.attack)
    print ("Here is the Zombie's Attack:", Zombie.attack)

    def compare_archerattack_zom():
        if Archer.attack > Zombie.attack:
            print ("You have won in this stat, good luck in the next.")
            zom_listy.append("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerattack_zom()

    input ("---")

    print ("Here is your Archer's health:", Archer.health)
    print ("Here is the Slime's health:", Slime.health)

    def compare_archerhealth_zom():
        if Archer.health > Slime.health:
            print ("You have won in this stat, good luck in the next.")
            zom_listy.append ("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerhealth_zom()

    input ("---")

    print ("Here is your Archer's speed:", Archer.speed)
    print ("Here is the Zombie's speed:", Zombie.speed)

    def compare_archerspeed_zom():
        if Archer.speed > Zombie.speed:
            print ("You have won in this stat, good luck in the next.")
            zom_listy.append ("1")
        else:
            print ("You have lost in this stat, better luck in the next one.")
    compare_archerspeed_zom()

    input ("---")

    def zom_winny():
        if len(zom_listy) > 1:
            print ("You have beaten the ZOMBIE, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    zom_winny()





def vs_Goba():

    print ("You have found a Goblin. Good luck")
    
    input ("---")
    
    print ("Here is The Goblin's attack", Goblin.attack)
    print ("Here are your Archers attack", Archer.attack)
    
    goblin_list = []
    
    def compare_goblin_attack():
        if Archer.attack > Goblin.attack:
            print ("You have won this stat, move on to the next.")
            goblin_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_goblin_attack()
    
    input ("---")
    
    print ("Here is The Goblin's health", Goblin.health)
    print ("Here are your Archers health", Archer.health) 
    
    def compare_goblin_health():
        if Archer.health > Goblin.health:
            print ("You have won this stat, move on to the next.")
            goblin_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_goblin_health()
    
    input ("---")
    
    print ("Here is The Goblin's speed", Goblin.speed)
    print ("Here are your Archers speed", Archer.speed) 
    
    
    def compare_goblin_speed():
        if Archer.speed > Goblin.speed:
            print ("You have won this stat, your fate will be revealed.")
            goblin_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed.")
    compare_goblin_speed()
    
    input ("---")
    
    def goblin_winny():
        if len(goblin_list) > 1:
            print ("You have beaten the GOBLIN, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    goblin_winny()



def vs_Skelea():

    print ("You have found a Skeleton. Good luck")

    input ("---")

    print ("Here is The Skeleton's attack", Skeleton.attack)
    print ("Here are your Archers attack", Archer.attack)

    skele_list = []

    def compare_skele_attack():
        if Archer.attack > Skeleton.attack:
            print ("You have won this stat, move on to the next.")
            skele_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_skele_attack()

    input ("---")

    print ("Here is The Skeleton's health", Skeleton.health)
    print ("Here are your Archers health", Archer.health) 

    def compare_skele_health():
        if Archer.health > Skeleton.health:
            print ("You have won this stat, move on to the next.")
            skele_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_skele_health()

    input ("---")

    print ("Here is The Skeleton's speed", Skeleton.speed)
    print ("Here are your Archers speed", Archer.speed) 


    def compare_skele_speed():
        if Archer.speed > Skeleton.speed:
            print ("You have won this stat, your fate will be revealed.")
            skele_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed")
    compare_skele_speed()

    input ("---")

    def skele_winny():
        if len(skele_list) > 1:
            print ("You have beaten the SKELETON, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    skele_winny()





def vs_Mina():

    print ("You have found a Minotaur. Good luck")

    input ("---")

    print ("Here is The Minotaur's attack", Minotaur.attack)
    print ("Here are your Archers attack", Archer.attack)

    min_list = []

    def compare_min_attack():
        if Archer.attack > Minotaur.attack:
            print ("You have won this stat, move on to the next.")
            min_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_min_attack()

    input ("---")

    print ("Here is The Minotaur's health", Minotaur.health)
    print ("Here are your Archers health", Archer.health) 

    def compare_min_health():
        if Archer.health > Minotaur.health:
            print ("You have won this stat, move on to the next.")
            min_list.append ("1")
        else: 
            print ("You lost for this stat, good luck in the next")
    compare_min_health()

    input ("---")

    print ("Here is The Minotaur's speed", Minotaur.speed)
    print ("Here are your Archers speed", Archer.speed) 


    def compare_min_speed():
        if Archer.speed > Minotaur.speed:
            print ("You have won this stat, your fate will be revealed.")
            min_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed")
    compare_min_speed()

    input ("---")

    def min_winny():
        if len(min_list) > 1:
            print ("You have beaten the MINOTAUR, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    min_winny()



def vs_Cyca():

    print ("You have found a Cyclops. Good luck")

    input ("---")

    print ("Here is The Cyclops's attack", Cyclops.attack)
    print ("Here are your Archers attack", Archer.attack)

    cyc_list = []

    def compare_cyc_attack():
        if Archer.attack > Cyclops.attack:
            print ("You have won this stat, move on to the next.")
            cyc_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_cyc_attack()

    input ("---")

    print ("Here is The Cyclops's health", Cyclops.health)
    print ("Here are your Archers health", Archer.health) 

    def compare_cyc_health():
        if Archer.health > Cyclops.health:
            print ("You have won this stat, move on to the next.")
            cyc_list.append ("1")
        else: 
            print ("You lost for this stat, good luck in the next")
    compare_cyc_health()

    input ("---")

    print ("Here is The Cyclops's speed", Cyclops.speed)
    print ("Here are your Archers speed", Archer.speed) 


    def compare_cyc_speed():
        if Archer.speed > Cyclops.speed:
            print ("You have won this stat, your fate will be revealed.")
            cyc_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed")
    compare_cyc_speed()

    input ("---")

    def cyc_winny():
        if len(cyc_list) > 1:
            print ("You have beaten the CYCLOPS, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    cyc_winny()





def vs_GSa():

    print ("You have found a Giant Spider. Good luck")

    input ("---")

    print ("Here is The Giant Spider's attack", GiantSpider.attack)
    print ("Here are your Archers attack", Archer.attack)

    GS_list = []

    def compare_GS_attack():
        if Archer.attack > GiantSpider.attack:
            print ("You have won this stat, move on to the next.")
            GS_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_GS_attack()

    input ("---")

    print ("Here is The Giant Spider's health", GiantSpider.health)
    print ("Here are your Archers health", Archer.health) 

    def compare_GS_health():
        if Archer.health > GiantSpider.health:
            print ("You have won this stat, move on to the next.")
            GS_list.append ("1")
        else: 
            print ("You lost for this stat, good luck in the next")
    compare_GS_health()

    input ("---")

    print ("Here is The Giant Spider's speed", GiantSpider.speed)
    print ("Here are your Archers speed", Archer.speed) 


    def compare_GS_speed():
        if Archer.speed > GiantSpider.speed:
            print ("You have won this stat, your fate will be revealed.")
            GS_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed")
    compare_GS_speed()

    input ("---")

    def GS_winny():
        if len(GS_list) > 1:
            print ("You have beaten the GIANT SPIDER, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    GS_winny()




def vs_yea():

    print ("You have found a Yeti. Good luck")

    input ("---")

    print ("Here is The Yeti's attack", Yeti.attack)
    print ("Here are your Archers attack", Archer.attack)

    ye_list = []

    def compare_ye_attack():
        if Archer.attack > Yeti.attack:
            print ("You have won this stat, move on to the next.")
            ye_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_ye_attack()

    input ("---")

    print ("Here is The Yeti's health", Yeti.health)
    print ("Here are your Archers health", Archer.health) 

    def compare_ye_health():
        if Archer.health > Yeti.health:
            print ("You have won this stat, move on to the next.")
            ye_list.append ("1")
        else: 
            print ("You lost for this stat, good luck in the next")
    compare_ye_health()

    input ("---")

    print ("Here is The Yeti's speed", Yeti.speed)
    print ("Here are your Archers speed", Archer.speed) 


    def compare_ye_speed():
        if Archer.speed > Yeti.speed:
            print ("You have won this stat, your fate will be revealed.")
            ye_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed")
    compare_ye_speed()

    input ("---")

    def ye_winny():
        if len(ye_list) > 1:
            print ("You have beaten the YETI, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    ye_winny()



def vs_hyda():

    print ("You have found a Hydra. Good luck")

    input ("---")

    print ("Here is The Hydra's attack", Hydra.attack)
    print ("Here are your Archers attack", Archer.attack)

    hyd_list = []

    def compare_hyd_attack():
        if Archer.attack > Hydra.attack:
            print ("You have won this stat, move on to the next.")
            hyd_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_hyd_attack()

    input ("---")

    print ("Here is The Hydra's health", Hydra.health)
    print ("Here are your Archers health", Archer.health) 

    def compare_hyd_health():
        if Archer.health > Hydra.health:
            print ("You have won this stat, move on to the next.")
            hyd_list.append ("1")
        else: 
            print ("You lost for this stat, good luck in the next")
    compare_hyd_health()

    input ("---")

    print ("Here is The Hydra's speed", Hydra.speed)
    print ("Here are your Archers speed", Archer.speed) 


    def compare_hyd_speed():
        if Archer.speed > Hydra.speed:
            print ("You have won this stat, your fate will be revealed.")
            hyd_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed")
    compare_hyd_speed()

    input ("---")

    def hyd_winny():
        if len(hyd_list) > 1:
            print ("You have beaten the HYDRA, good luck on your next FOE")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            exit()
    hyd_winny()




def vs_wrma():

    print ("You have found THE nelahWrM. This is the final boss. Good luck")

    input ("---")

    print ("Here is The nelahWrM's attack", nelahWrM.attack)
    print ("Here are your Archers attack", Archer.attack)

    wrm_list = []

    def compare_wrm_attack():
        if Archer.attack > nelahWrM.attack:
            print ("You have won this stat, move on to the next.")
            wrm_list.append ("1")
        else:
            print ("You lost for this stat, good luck in the next")
    compare_wrm_attack()

    input ("---")

    print ("Here is The nelahWrM's health", nelahWrM.health)
    print ("Here are your Archers health", Archer.health) 

    def compare_wrm_health():
        if Archer.health > nelahWrM.health:
            print ("You have won this stat, move on to the next.")
            wrm_list.append ("1")
        else: 
            print ("You lost for this stat, good luck in the next")
    compare_wrm_health()

    input ("---")

    print ("Here is The nelahWrM's speed", nelahWrM.speed)
    print ("Here are your Archers speed", Archer.speed) 


    def compare_wrm_speed():
        if Archer.speed > Hydra.speed:
            print ("You have won this stat, your fate will be revealed.")
            wrm_list.append ("1")
        else:
            print ("You lost for this stat, your fate will be revealed")
    compare_wrm_speed()

    input ("---")

    def wrm_winny():
        if len(wrm_list) > 1:
            input ("You have beaten NELAHWRM...")
            input ("the WORLD...")
            input ("is LIBERATED")
        else:
            input ("You have lost ...")
            input ("your figure ... splintered")
            input ("... your enemy has landed a ... fatal blow")
            input ("Nelahwrm's reign will continue unphased")
            input ("...")
            input ("This WORLD shall know PAIN")
            exit()
    wrm_winny()
