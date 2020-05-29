N = int(input())
time = 0
A = []
for i in range(N):
    a,b = map(int, input().split())
    A.append([b,a])
A.sort()
for i in range(N):
    time += A[i][1]
    if time > A[i][0]:
        print("No")
        exit()
print("Yes")