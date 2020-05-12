N,M = map(int, input().split())
res = [0]*M
for i in range(N):
    A = list(map(int, input().split()))
    K = A[0]
    for j in range(1,K+1):
        res[A[j]-1] += 1
print(res.count(N))