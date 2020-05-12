N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [0]*N #各場所に最初に到着するまでの移動回数
cnt = 0 #現在の移動回数
pos = 0 #現在の場所
flag = False
while K > 0:
    cnt += 1
    K -= 1
    if visited[pos] == 0:
        visited[pos] = cnt
    elif not flag:
        K %= cnt-visited[pos]
        flag = True
    pos = A[pos]-1
print(pos+1)