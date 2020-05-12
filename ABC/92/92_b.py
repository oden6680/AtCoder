N = int(input())
D,X = map(int, input().split())
cnt = X+N
for i in range(N):
    a = int(input())
    j = 1
    while a*j+1 <= D:
        j += 1
        cnt += 1
print(cnt)