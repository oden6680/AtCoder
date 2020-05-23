N,K = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l, reverse = True)
res = 0
for i in range(K):
    res += l[i]
print(res)