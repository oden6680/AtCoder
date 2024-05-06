N, X, Y = map(int, input().split())
res = [0] * (N-1)

for i in range(1, N):
    for j in range(i+1, N+1):
        dis = min(j-i, abs(X-i) + abs(Y-j) + 1)
        res[dis - 1] += 1

for i in range(N-1):
    print(res[i])