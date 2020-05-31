N = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
res = 0
for i in range(1,2*N,2):
    res += a[i]
print(res)