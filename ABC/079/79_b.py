N = int(input())
A =[2,1]
if N < 2:
    print(A[N])
    exit()
for i in range(2,N+1):
    A.append(A[i-1]+A[i-2])
print(A[-1])