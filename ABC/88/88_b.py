N = int(input())
a = list(map(int, input().split()))
Alice = 0
Bob = 0
a = sorted(a,reverse = True)
for i in range(N):
    if (i+1)%2 == 1:
        Alice += a[i]
    else:
        Bob += a[i]
print(Alice-Bob)