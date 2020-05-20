N = int(input())
a = list(map(int, input().split()))
if sum(a)%N != 0:
    print(-1)
    exit()
else:
    ave = sum(a)//N
    cnt = 0
res = 0
SUM = 0
for i in range(N):
    cnt += 1
    SUM += a[i]
    if SUM%cnt == 0 and SUM//cnt == ave:
        res += cnt-1
        SUM = 0
        cnt = 0
res += cnt
print(res)