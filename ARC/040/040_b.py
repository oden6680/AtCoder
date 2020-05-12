N,R = map(int, input().split())
S = input()
perfect = ['o']*N
r_i = S.rfind('.')
S = list(S)
res = 0
k = 0
while S != perfect:
    if k+R-1 >= r_i:
        res += 1
        break
    if S[k] == '.':
        res += 1
        for j in range(k,min(N,k+R)):
            S[j] = 'o'
    else:
        k += 1
        res += 1
print(res)