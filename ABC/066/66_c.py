from collections import deque
n = int(input())
a = list(map(str, input().split()))
b = deque()
if n%2:
    flag = False
else:
    flag = True
for i in range(n):
    if flag:
        if (i+1)%2:
            b.append(a[i])
        else:
            b.appendleft(a[i])
    else:
        if (i+1)%2:
            b.appendleft(a[i])
        else:
            b.append(a[i])
res = list(b)
print(' '.join(res))