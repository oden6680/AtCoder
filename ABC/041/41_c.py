N = int(input())
a = list(map(int, input().split()))
res = [(0,0)]*N
for i in range(N):
    res[i] = [a[i],i+1]
res = sorted(res, reverse = True)
for i in range(N):
    print(res[i][1])