N,K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
R = R[N-K:N]
reat = 0
for i in range(K):
    reat = (reat+R[i])/2
print(reat)