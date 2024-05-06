X, N = map(int, input().split())
if N > 0:
    p = list(map(int, input().split()))
elif N == 0:
    print(X)
    exit()
else :
    p = [int(input())]
if N == 100:
    if X <= 50:
        print(0)
    else:
        print(101)
    exit()

for i in range(X+1):
    if not i in p:
        x = i

for i in range(X,101):
    if not i in p:
        y = i
        break
    elif i == 100:
        y = 101

if (X-x) == (y-X):
    print(x)
elif (X-x) > (y-X):
    print(y)
else:
    print(x)