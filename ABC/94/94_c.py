N = int(input())
X = list(map(int, input().split()))
sort_X = sorted(X)
L = sort_X[(N//2)-1]
R = sort_X[N//2]
for i in range(N):
    if X[i] <= L:
        print(R)
    else:
        print(L)