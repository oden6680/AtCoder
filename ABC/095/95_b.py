N,X = map(int, input().split())
M = []
for i in range(N):
    m = int(input())
    M.append(m)
res = X - sum(M)
print(N+res//min(M))