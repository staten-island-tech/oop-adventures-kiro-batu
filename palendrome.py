x = input ("Input a palendrome: ")

def pal (x):
    y = x[::-1]
    if y == x:
        print ("This is a palendrome")
    else:
        print ("This is not a palendrome")
pal(x)