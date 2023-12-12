x=input ("Put in an number: ")

def isISBN():
    if len(x) == 10 or len(x) == 13:
        print ("True")
    else:
        print ("False")
isISBN()