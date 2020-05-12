n,d = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
for i in range(n-1):
    for j in range(i+1,n):
        s = 0
        for k in range(d):
            s+=(abs(a[i][k]-a[j][k]))**2
        if s**0.5==int(s**0.5):
            cnt+=1
print(cnt)