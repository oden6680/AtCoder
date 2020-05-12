a,b,k = map(int, input().split())
if k >= a:
    k = k-a
    a = 0
else:
    a -= k

if k >= b:
    b = 0
else :
    b -= k
print(a,b)