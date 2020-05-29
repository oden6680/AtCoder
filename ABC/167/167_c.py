N,M,X = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(N)]
res = float('inf') #無限で初期化
for i in range(2**N):
    tca = [0]*(M+1) #index(0)=totalcost
    for j in range(N):
        if (i >> j) & 1:#その本を使うかどうかの判定
            for k in range(M+1):
                tca[k] += ca[j][k]
    if min(tca[1:]) >= X:
        res = min(res, tca[0])

if res != float('inf'):
    print(res)
else:
    print(-1)