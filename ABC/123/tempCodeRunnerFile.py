A = [int(input()) for _ in range(5)]
cnt = 0
Max = 0
for i in range(len(A)):
    if A[i]%10 > Max:
        Max = i
for i in range(len(A)):
    if i != Max:
        cnt += A[i]
    while cnt%10 != 0:
        cnt += 1
print(cnt+A[Max])