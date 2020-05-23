N = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())
NG = [NG1,NG2,NG3]
if N in NG:
    print("NO")
    exit()
cnt = 0
while N > 0:
    if cnt >= 100:
        print("NO")
        exit()
    if not N-3 in NG:
        N -= 3
    elif not N-2 in NG:
        N -= 2
    elif not N-1 in NG:
        N -= 1
    else:
        print("NO")
        exit()
    cnt += 1
print("YES")