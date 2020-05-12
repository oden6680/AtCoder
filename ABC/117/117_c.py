N,M = map(int, input().split())
X = list(map(int, input().split()))
if M <= N:
    print(0)
    exit()
X.sort()
L = []
for i in range(1,M):
    L.append(X[i]-X[i-1])
L.sort()
L.reverse()
res = sum(L)
for i in range(N-1):
    res -= L[i]
print(res)