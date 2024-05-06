N = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(1,N):
    if a[i-1] == a[i]:
        a[i] = 0
        cnt += 1
print(cnt)