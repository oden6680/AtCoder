N = int(input())
res = set()
for i in range(N):
    a = int(input())
    res.add(a)
res = list(res)
res.sort()
print(res[-2])