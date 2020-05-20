N,Q = map(int, input().split())
res = [0]*N
for i in range(Q):
    l,r,t = map(int, input().split())
    for j in range(l-1,r):
        res[j] = t
for i in range(N):
    print(res[i])