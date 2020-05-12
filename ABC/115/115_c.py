N,K = map(int, input().split())
h = []
for i in range(N):
    h.append(int(input()))
h.sort()
res = 10**9
for i in range(N-K):
    if res > h[i+K-1]-h[i]:
        res = h[i+K-1]-h[i]
print(res)