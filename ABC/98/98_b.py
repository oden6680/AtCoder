N = int(input())
S = list(input())
max_cnt = 0
for i in range(1,N-1):
    L = S[0:i]
    R = S[i:N]
    temp = len(set(L)&set(R))
    if temp > max_cnt:
        max_cnt = temp
print(max_cnt)