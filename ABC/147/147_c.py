N = int(input())
A = []
xy = []

for i in range(N):
    a = int(input())
    tmp = []
    for j in range(a):
        x,y = map(int, input().split())
        tmp.append([x-1,y])
    A.append(a)
    xy.append(tmp)

res = 0
for i in range(2**N):
    cnt = 0
    contra = False
    for j in range(N):
        if (i >> j) & 1 and contra == False: #正直者の時
            cnt += 1
            temp = xy[j]
            for x, y in temp:
                if (i >> x) & 1 != y:
                    contra = True
                    break
    if contra == False:
        res = max(res,cnt)
print(res)