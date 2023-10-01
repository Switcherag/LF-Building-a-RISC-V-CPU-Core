## BLT 	Branch if less than 	(x1 < x2) ^ (x1[31] != x2[31])

# define x1 and x2 as BYTE signed
x1 = 0b0000
x2 = 0b1000


def BLT(a,b):
    print("BLT")
    if (a >= b) ^ (a & 0b1000 != b & 0b1000):
        print("sign",a & 0b1000 != b & 0b1000) 
        return True
    else:
        
        return False

def BLTU(a,b):
    print("BLTU")
    if a >= b:
        return True
    else:
        return False

print(BLT(x1,x2))
print(BLTU(x1,x2))