N = int(input())
a = list(map(int, input().split()))
cnt = 0
flag = True
for i in range(N):
    while a[i]%2 == 0:
        if flag:
            flag = False
        a[i] = a[i]//2
        cnt += 1
if flag:
    print(0)
else:
    print(cnt)