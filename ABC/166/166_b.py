N,K = map(int, input().split())
A = [0]*N
for i in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        A[a[j]-1] = 1
res = 0
for i in range(N):
    if A[i] == 0:
        res += 1
print(res)