n = int(input())
res = []
for i in range(n):
    s,p = input().split()
    p = int(p)
    res.append((s,-p,i+1))
res.sort()
for i in range(n):
    print(res[i][2])