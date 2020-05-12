n,k,m = map(int, input().split())
a = map(int, input().split())
sm = sum(a)
if m*n - sm <= k :
    if m*n - sm > 0 :
        print(m*n-sm)
    else :
        print(0)
else:
    print (-1)