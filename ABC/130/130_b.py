n,x = map(int, input().split())
l = list(map(int, input().split()))
flag = 0
d = []
d.append(0)
for i in range(1,n+1):
    if d[i-1]+l[i-1] > x:
        break
    else:
        d.append(d[i-1]+l[i-1])
print(len(d))