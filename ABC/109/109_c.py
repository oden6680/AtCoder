from fractions import gcd
N,X = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
b = [abs(X-x[i]) for i in range(N)]
ans = b[0]
for i in range(N-1):
  ans = gcd(ans,b[i+1])
print(ans)