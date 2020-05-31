N = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(N):
    if i+1 == a[a[i]-1]:
        res += 1
print(res//2)