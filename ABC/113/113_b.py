N = int(input())
T,A = map(int, input().split())
H = list(map(int, input().split()))
min_dif = 10**9
for i in range(N):
    dif = abs(A-(T-H[i]*0.006))
    if min_dif > dif:
        min_dif = dif
        res_i = i
print(res_i+1)