N = int(input())
a = list(map(int, input().split()))
x = a[0]
y = sum(a)-a[0]
res = abs(x-y)
for i in range(1,N-1):
    x += a[i]
    y -= a[i]
    if abs(x-y) < res:
        res = abs(x-y)
print(res)