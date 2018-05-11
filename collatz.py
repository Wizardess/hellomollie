def collatz(z):
    if z == 1:
        print("Three cheers to Collatz!")
    elif z%2 == 0:
        print(int(z/2))
        collatz(int(z/2))
    else:
        print(3*z+1)
        collatz(3*z+1)

def colWhile(z):
    i = 0
    while z != 1:
        if z%2 == 0:
            z = int(z/2)
        else:
            z = 3*z + 1
        i += 1
    return True, i
        
print(colWhile(5692874))