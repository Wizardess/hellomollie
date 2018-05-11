O = "TO INFINITY...AND BEYOND!"

def pointCalc(p1,p2,m):
    x3 = m**2 - p1[0] - p2[0]
    y3 = m*(p1[0] - x3) - p1[1]
    return (x3, -y3)

def slopeCalc_diff(p1,p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def slopeCalc_same(p1,A):
    return (3*(p1[0]**2) + A) / (2*p1[1])

def findp3(p1,p2,A):
    if p1 == O:
        p3 = p2
    elif p2 == O:
        p3 = p1
    elif p1[0] == p2[0] and p1[1] == -p2[1]:
        p3 = O
    elif p1 == p2:
        p3 = pointCalc(p1,p1,slopeCalc_same(p1,A))
    else:
        p3 = pointCalc(p1,p2,slopeCalc_diff(p1,p2))
    return p3

print(findp3((7,16),(1,2),-15))
    