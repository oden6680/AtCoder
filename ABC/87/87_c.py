N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
res = 0
if N == 1:
    print(A1[0]+A2[0])
    exit()
for i in range(2):
    for j in range(N):
        temp = sum(A1[i:j])+sum(A2[j-1:N])
        if temp > res:
            res = temp
print(res)