A = [int(input()) for _ in range(5)]
cnt = 0
Max = 10
Max_i = 0
for i in range(len(A)):
    if 0 < A[i]%10 < Max:
        Max = A[i]%10
        Max_i = i
for i in range(len(A)):
    if i != Max_i:
        cnt += A[i]
    while cnt%10 != 0:
        cnt += 1
print(cnt+A[Max_i])