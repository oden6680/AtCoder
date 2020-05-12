n = int(input())
h = list(int(i) for i in input().split())
res = h[0]
for i in range(n-1):
    if h[i]<h[i+1]:
        res += h[i+1]-h[i]
print(res)