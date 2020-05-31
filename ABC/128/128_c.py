N,M = map(int, input().split())
switch_inf = []
for i in range(M):
    temp  = list(map(int, input().split()))
    switch_inf.append(temp)
p = list(map(int, input().split()))

res = 0
for i in range(2**N):#bit全探索開始
    switch = [0]*N
    for j in range(N):
        if (i >> j) & 1:
            switch[j] = 1
    light_cnt = 0 #点灯しているライトの数
    for j in range(M): #スイッチの情報から転倒するものを探索
        cnt = 0 #ライト_jにおいて押されているスイッチの数
        for k in range(1,switch_inf[j][0]+1):
            if switch[switch_inf[j][k]-1]:
                cnt += 1
        if cnt%2 == p[j]:
            light_cnt += 1
    if light_cnt == M:
        res += 1
print(res)