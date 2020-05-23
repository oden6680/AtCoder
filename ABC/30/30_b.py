n,m = map(int, input().split())
if n >= 12:
    n -= 12
hour = 30*n + 0.5*m
minit = 6*m
res = max(hour,minit)-min(hour,minit)
print(min(res,360-res))