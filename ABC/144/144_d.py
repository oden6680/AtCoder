import math
a,b,x = map(int, input().split())
if x >= a*a*b/2:
    X = (2*a*a*b-2*x)/(a**3)
    print(math.degrees(math.atan(X)))
else:
    X = (a*b*b)/(2*x)
    print(math.degrees(math.atan(X)))