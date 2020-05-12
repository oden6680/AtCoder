import math
k = int(input())
cnt = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for p in range(1,k+1):
            cnt += math.gcd(math.gcd(i,j),p)
print(cnt)