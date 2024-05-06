K, N = map(int, input().split())
A = list(map(int, input().split()))
dis = []
res = 0
for i in range(1,N):
    res += A[i]-A[i-1]
    dis.append(A[i]-A[i-1])
dis.append(K - A[N-1] + A[0])
res += K - A[N-1] + A[0] - max(dis)

print(res)