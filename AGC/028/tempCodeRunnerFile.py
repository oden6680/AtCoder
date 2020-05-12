from fractions import gcd
N, M = list(map(int, input().split()))
S = input()
T = input()
d = gcd(N,M)
n = N//d
m = M//d
for i in range(d):
    if S[i*n] != T[i*m]:
        flag = True
    else:
        flag = False
if flag:
  print((N*M)//d)
else:
  print(-1)