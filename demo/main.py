from merchant import Merchant
from hero import Hero
#Creates a new instance of Merchant, Instantiation?
Batu = Merchant ("Batu", ["Sea Shell", "Green Sweater", "Jarvis", "Soul"])
Hambergs = Hero("Amber",500, ["Hamburger"])
item = Batu.sell ("Soul")
print (item)
Hambergs.buy (item)