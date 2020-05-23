N = int(input())
res = [0,0,1]
for i in range(N-3):
    res.append((res[-1]+res[-2]+res[-3])%10007)
print(res[N-1]%10007)