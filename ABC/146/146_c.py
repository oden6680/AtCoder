A,B,X = map(int,input().split())
res = 0
right = 10**9 + 1
while res + 1 != right:
    mid = int((res + right)/2)
    if A*mid + B*len(str(mid)) <= X:
        res = mid
    else:
        right = mid
print(res)