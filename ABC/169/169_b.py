N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
res = A[0]
for i in range(1,N):
    res *= A[i]
    if res > 10**18:
        print(-1)
        exit()
print(res)