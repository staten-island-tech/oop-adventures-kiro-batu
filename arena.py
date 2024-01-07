import random
## Import the types of troops
from troops import Cavalry, Archer, Infantry

##Import the enemies
from enemies import Slime, Zombie, Goblin, Skeleton, Minotaur, Cyclops, GiantSpider, Yeti, Hydra, nelahWrM
from __archer import  vs_slimea, vs_Goba, vs_zoma, vs_Skelea, vs_Mina, vs_Cyca, vs_hyda, vs_GSa, vs_wrma, vs_yea, slime_defeat, troopslime
from __infantry import   vs_slimei, vs_Gobi, vs_zomi, vs_Skelei, vs_Mini, vs_Cyci, vs_hydi, vs_GSi, vs_wrmi, vs_yei, slime_defeat, troopslime
from __cavalry import vs_slimec, vs_Gobc, vs_zomc, vs_Skelec, vs_Minc, vs_Cycc, vs_hydc, vs_GSc, vs_wrmc, vs_yec, slime_defeat, troopslime

trooplist = ["Cavalry", "Archer", "Infantry" ]
troopinput = ("Select a troop type to send out into battle: ")

def cal():
    print("You have selected the Cavalry: your current stats will be printed ")
    print ("- Attack: ", Cavalry.attack)
    print ("- Speed: ", Cavalry.speed )
    print ("- Health: ", Cavalry.health)
   
def arc():
    print("You have selected the Archer: your current stats will be printed ")
    print ("- Attack: ", Archer.attack)
    print ("- Speed: ", Archer.speed )
    print ("- Health: ", Archer.health)

def inf():
    print("You have selected the Infantry: your current stats will be printed ")
    print ("- Attack: ", Infantry.attack)
    print ("- Speed: ", Infantry.speed )
    print ("- Health: ", Infantry.health)
    
def beforearena():
    print("Before entering the next battle, you're current stats will be shown ")
    print ("- Cavalry: Attack: ", Cavalry.attack)
    print ("- Cavlary: Speed: ", Cavalry.speed )
    print ("- Cavalry: Health: ", Cavalry.health)
    input("---")
    print ("- Archer: Attack: ", Archer.attack)
    print ("- Archer: Speed: ", Archer.speed )
    print ("- Archer: Health: ", Archer.health)
    input("---")
    print ("- Infantry: Attack: ", Infantry.attack)
    print ("- Infantry: Speed: ", Infantry.speed )
    print ("- Infantry: Health: ", Infantry.health)

def slimebattle():
    trooplist = ["Cavalry", "Archer", "Infantry" ]

    input ("You're now engaged within a battle with the devilish SLIME ")
    input ("It JIGGLED it's way to your feet ")
    input ("It attempted to SWALLOW your SHOE ")
    input ("---")
    print("Slime: Attack: ", Slime.attack)
    print("Slime: Speed:", Slime.speed)
    print("Slime: Health: ", Slime.health)
    print("---")
    troopinput = input("-Select a troop type to send out into battle: ")

    if troopinput == ("Cavalry"):
        print("---")
        cal()
        print("---")
        vs_slimec()
    elif troopinput == ("Archer"):
        print("---")
        arc()
        print("---")
        vs_slimea()
    if troopinput == ("Infantry"):
        print("---")
        inf()
        print("---")
        vs_slimei()

    if not troopinput in trooplist:
            print ("---")
            print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
            input ("---")
            return slimebattle()
            


def nextarena():
    troopinput = ["Cavalry", "Archer", "Infantry"]
    print ("The BATTLES continuing this point will be more fulfilling")
    
    start = 1
    end = 4
    
    values = list(range(start,end))
    global mon_choicena
    mon_choicena = random.choice(values)

    if mon_choicena == (1):
        input ("You've engaged in a battle with a demonic ZOMBIE ")
        input ("It BELLOWED the phrase BRAINZ, ")
        input ("It began INCHING towards you ")
        input ("---")
        print ("Zombie: Attack:", Zombie.attack)
        print ("Zombie: Speed:", Zombie.speed)
        print ("Zombie: Health", Zombie.health)
    elif mon_choicena == (2):
        input ("You've engaged in a battle with a ghastly SKELETON ")
        input ("It's entire body began RATTLING ")
        input ("It SWIPPED it's rusted SWORD ")
        input ("---")
        print ("Skeleton: Attack:", Skeleton.attack)
        print ("Skeleton: Speed:", Skeleton.speed)
        print ("Skeleton: Health:", Skeleton.health)
    if mon_choicena == (3):
        input ("You've engaged in a battle with a cheeky GOBLIN ")
        input ("It SNICKERED as it praised its treasure ")
        input ("It began to BOUNCE around with gold FLYING about ")
        input ("---")
        print ("Goblin: Attack:", Goblin.attack)
        print ("Goblin: Speed:", Goblin.speed)
        print ("Goblin: Health:", Goblin.health)
    
def nextarenafight():
    troopinput = input("Select a troop type to send out into battle: ")

    while troopinput == ("Cavalry"):
        print("---")
        cal()
        if mon_choicena == (1):
            print("---")
            vs_Gobc
        if mon_choicena == (2):
            print("---")
            vs_zomc
        if mon_choicena == (3):
            print("---")
            vs_Skelec
        break

    while troopinput == ("Archer"):
        print("---")
        arc()
        if mon_choicena == (1):
            print("---")
            vs_Goba
        if mon_choicena == (2):
            print("---")
            vs_zoma
        if mon_choicena == (3):
            print("---")
            vs_Skelea
        break

    while troopinput == ("Infantry"):
        print("---")
        inf()
        if mon_choicena == (1):
            print("---")
            vs_Gobi
        if mon_choicena == (2):
            print("---")
            vs_zomi
        if mon_choicena == (3):
            print("---")
            vs_Skelei
        break

    if not troopinput in trooplist:
            print ("---")
            print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
            input ("---")
            return nextarenafight()


def minoboss():
    input ("You've encountered your first boss traveler ")
    input ("THE MIGHTY MINOTAUR shall be your opponent ")
    input ("---")
    input ("It began to HUFF and PUFF, STEAM shot out of its SNOUT ")
    input ("It began to STRIKE its hooves at the ground, it was ready to CHARGE ")

    print("Minotaur: Attack: ", Minotaur.attack)
    print("Minotaur: Speed: ", Minotaur.speed)
    print("Minotaur: Health: ", Minotaur.health)

    troopinput = input("Select a troop type to send out into battle: ")
    if troopinput == ("Cavalry"):
        print("---")
        cal()
        print("---")
        vs_Minc()
    elif troopinput == ("Archer"):
        print("---")
        arc()
        print("---")
        vs_Mina()
    if troopinput == ("Infantry"):
        print("---")
        inf()
        print("---")
        vs_Mina()
    if not troopinput in trooplist:
            print ("---")
            print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
            input ("---")
            return minoboss()


def colcavern():
    start = 1
    end = 3
    
    values = list(range(start,end))
    global mon_choicenea
    mon_choicenea = random.choice(values)
    

    if mon_choicenea == (1):
        input ("You've engaged in a battle with a mighty MINOTAUR ")
        input ("It began to HUFF and PUFF, STEAM shot out of its SNOUT ")
        input ("It began to STRIKE its hooves at the ground, it was ready to CHARGE ")
        input ("---")
        print ("Minotaur: Attack:", Minotaur.attack)
        print ("Minotaur: Speed:", Minotaur.speed)
        print ("Minotaur: Health", Minotaur.health)
    elif mon_choicenea == (2):
        input("You've engaged in a battle with a cynical CYCLOPS ")
        input("It CHOWED down on a chunk of MEAT ")
        input("It began to MENACING STARE at you with it LONE EYE ")
        input ("---")
        print ("Cyclops: Attack:", Cyclops.attack)
        print ("Cyclops: Speed:", Cyclops.speed)
        print ("Cyclops: Health:", Cyclops.health)

    
def colcavernfight():
    troopinput = input("Select a troop type to send out into battle: ")

    while troopinput == ("Cavalry"):
        print("---")
        cal()
        if mon_choicenea == (1):
            print("---")
            vs_Minc
        if mon_choicenea == (2):
            print("---")
            vs_Cycc
        break

    while troopinput == ("Archer"):
        print("---")
        arc()
        if mon_choicenea == (1):
            print("---")
            vs_Mina
        if mon_choicenea == (2):
            print("---")
            vs_Cyca
        break

    while troopinput == ("Infantry"):
        print("---")
        inf()
        if mon_choicenea == (1):
            print("---")
            vs_Mini
        if mon_choicenea == (2):
            print("---")
            vs_Cyci
        break
    
    if not troopinput in trooplist:
            print ("---")
            print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
            input ("---")
            return colcavernfight()



def GSboss ():
    input("You've encountered your first boss traveler ")
    input("THE GINORMOUS GIANT SPIDER shall be your opponent ")
    input("---")
    input("It SPUN around in its WEB, biding its TIME ")
    input("Suddenly it FANGS were perpendicular to your HEAD, as it LAUNCHED itself ")
    input("---")
    print("Giant Spider: Attack: ", GiantSpider.attack)
    print("Giant Spider: Speed: ", GiantSpider.speed)
    print("Giant Spider: Health: ", GiantSpider.health)

    troopinput = input("Select a troop type to send out into battle: ")
    if troopinput == ("Cavalry"):
        print("---")
        cal()
        print("---")
        vs_GSc()
    elif troopinput == ("Archer"):
        print("---")
        arc()
        print("---")
        vs_GSa()
    if troopinput == ("Infantry"):
        print("---")
        inf()
        print("---")
        vs_GSi()
    if not troopinput in trooplist:
            print ("---")
            print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
            input ("---")
            return GSboss()

def mountaintopofgi():
    start = 1
    end = 3
    
    values = list(range(start,end))
    global mon_choiceneea
    mon_choiceneea = random.choice(values)
    

    if mon_choiceneea == (1):
        input ("You've engaged in a battle with a ginormous GIANT SPIDER")
        input ("It SPUN its silk, biding its TIME")
        input ("Suddenly it FANGS were perpendicular to your HEAD, as it LAUNCHED itself")
        input ("---")
        print ("Giant Spider: Attack:", GiantSpider.attack)
        print ("Giant Spider: Speed:", GiantSpider.speed)
        print ("Giant Spider: Health", GiantSpider.health)
    elif mon_choiceneea == (2):
        input ("The air grew FRIGID ")
        input ("You've engaged in a battle with a yellow YETI ")
        input ("Snowflakes DESCENDED from the SKY ")
        input ("---")
        print ("Yeti: Attack:", Yeti.attack)
        print ("Yeti: Speed:", Yeti.speed)
        print ("Yeti: Health:", Yeti.health)

def mountaintopofgifi():

    troopinput = input("Select a troop type to send out into battle: ")

    while troopinput == ("Cavalry"):
        print("---")
        cal()
        if mon_choicenea == (1):
            print("---")
            vs_Minc
        if mon_choiceneea == (2):
            print("---")
            vs_Cycc


    while troopinput == ("Archer"):
        print("---")
        arc()
        if mon_choiceneea == (1):
            print("---")
            vs_Mina
        if mon_choiceneea == (2):
            print("---")
            vs_Cyca

    while troopinput == ("Infantry"):
        print("---")
        inf()
        if mon_choiceneea == (1):
            print("---")
            vs_Mini
        if mon_choiceneea == (2):
            print("---")
            vs_Cyci
    
    if not troopinput in trooplist:
            print ("---")
            print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
            input ("---")
            return mountaintopofgifi()
    
def hydraboss():
    input ("You've encountered the final servant of Nelahwrm")
    input ("THE HORRID HYDRA shall be your opponent")
    input ("---")
    input ("Each head presented its HATRED")
    input ("Their SCALES began to GLOW")
    input ("A WAVE of FIRE suddenly escaped ")
    input ("---")
    print ("Hydra: Attack: ", Hydra.attack)
    print ("Hydra: Speed: ", Hydra.speed)
    print ("Hydra: Health: ", Hydra.health)

    troopinput = input("Select a troop type to send out into battle: ")
    if troopinput == ("Cavalry"):
        print("---")
        cal()
        print("---")
        vs_hydc()
    elif troopinput == ("Archer"):
        print("---")
        arc()
        print("---")
        vs_hyda()
    if troopinput == ("Infantry"):
        print("---")
        inf()
        print("---")
        vs_hydi()
    if not troopinput in trooplist:
            print ("---")
            print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
            input ("---")
            return hydraboss()

def Nelahwrmfight():
    input ("You've stood eye to eye with Nelahwrm")
    input ("Stand proud, for the NEFARIOUS NELAHWRM shall be your opponent")
    input ("---")
    input ("There was an overwhelming SENSE OF WICKEDNESS")
    input ("NELAHWRM clutched his SPEAR")
    input ("He TOOK off from the GROUND")
    input ("His SPEAR had point to OBLITERATE YOU")
    input ("---")
    print("Nelahwrm: Attack: ", nelahWrM.attack)
    print("Nelahwrm: Speed: ", nelahWrM.speed)
    print("Nelahwrm: Health: ", nelahWrM.health)

    troopinput = input("Select a troop type to send out into battle: ")
    if troopinput == ("Cavalry"):
        print("---")
        cal()
        print("---")
        vs_wrmc()
    elif troopinput == ("Archer"):
        print("---")
        arc()
        print("---")
        vs_wrma()
    if troopinput == ("Infantry"):
        print("---")
        inf()
        print("---")
        vs_wrmi()
    if not troopinput in trooplist:
            print ("---")
            print ("This choice was not valid with your current figures. Remember, Archer, Infantry, or Cavalry.")
            input ("---")
            return Nelahwrmfight()



    

