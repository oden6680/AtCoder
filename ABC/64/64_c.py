N = int(input())
a = list(map(int, input().split()))
A = [0]*9
for i in range(N):
    if a[i] < 400:
        A[0] = 1
    elif a[i] < 800:
        A[1] = 1
    elif a[i] < 1200:
        A[2] = 1
    elif a[i] < 1600:
        A[3] = 1
    elif a[i] < 2000:
        A[4] = 1
    elif a[i] < 2400:
        A[5] = 1
    elif a[i] < 2800:
        A[6] = 1
    elif a[i] < 3200:
        A[7] = 1
    else:
        A[8] += 1
print(max(1,sum(A[:8])),sum(A[:8])+A[8])