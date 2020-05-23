N,M = map(int, input().split())
res = [0]*N
for i in range(M):
    a,b = map(int, input().split())
    res[a-1] += 1
    res[b-1] += 1
for i in range(N):
    print(res[i])