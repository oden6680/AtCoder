N,M = map(int, input().split())
a = []
b = []
c = []
d = []
#入力
for i in range(N):
    A,B = map(int, input().split())
    a.append(A)
    b.append(B)
for i in range(M):
    C,D = map(int, input().split())
    c.append(C)
    d.append(D)

res_min = [10**9]*N #各人の最小距離
res = [0]*N #出力する答え

#全探索
for i in range(N):
    for j in range(M):
        temp = abs(a[i]-c[j]) + abs(b[i]-d[j])
        if res_min[i] > temp:
            res_min[i] = temp
            res[i] = j+1
for i in range(N):
    print(res[i])