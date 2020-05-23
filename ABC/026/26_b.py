import math
N = int(input())
R = []
res = 0
for i in range(N):
    r = int(input())
    R.append(r)
R.sort()
for i in range(N):
    if (i+1)%2:
        res += R[i]**2 
    else:
        res -= R[i]**2
print(abs(res*math.pi))