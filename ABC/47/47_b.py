W,H,N = map(int, input().split())
l = 0
r = W
row = 0
up = H
for i in range(N):
    x,y,a = map(int, input().split())
    if a == 1:
        if x > l:
            l = x
    elif a == 2:
        if x < r:
            r = x
    elif a == 3:
        if y > row:
            row = y
    elif a == 4:
        if y < up:
            up = y
print(max(max((r-l),0)*max((up-row),0),0))