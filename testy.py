from enemies import Slime
from troops import Archer

def add():
    print (Slime.attack)
    print (Archer.attack)
    NewAttack = (Slime.attack + Archer.attack)
    print (NewAttack)
add()