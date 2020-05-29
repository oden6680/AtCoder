import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort()
res = 0
for i in range(N): #aを決定
    for j in range(i+1, N): #bを決定
        c = L[i] + L[j] #cの最大値を決定
        pos = bisect.bisect_left(L, c)
        res += max(0, pos-j-1)
print(res)