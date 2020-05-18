x = int(input())
q = x%11
if q == 0:
    print(2*(x//11))
elif q <= 6:
    print(2*(x//11)+1)
else:
    print(2*(x//11)+2)