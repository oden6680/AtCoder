N,M,X = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*N
for i in range(M):
    S[A[i]] = 1
sum_l = sum(S[0:X+1])
sum_r = sum(S[X+1:N])
print(min(sum_l,sum_r))