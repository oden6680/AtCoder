K,S = map(int, input().split())
cnt = 0
for i in range(K+1):
    for j in range(K+1):
        z = S-(i+j)
        if 0 <= z <= K:
            cnt += 1
print(cnt)