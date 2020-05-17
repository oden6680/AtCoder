N,M = map(int, input().split())
one2other = [0]*N
other2goal = [0]*N
for i in range(M):
    a,b = map(int, input().split())
    if a == 1:
        one2other[b-1] = 1
    if b == N:
        other2goal[a-1] = 1
for i in range(N):
    if one2other[i] == 1 and other2goal[i] == 1:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")