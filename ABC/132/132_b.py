n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(1,n-1):
    if (p[i-1] > p[i] and p[i+1] < p[i]) or (p[i-1] < p[i] and p[i+1] > p[i]):
        cnt += 1
print(cnt)