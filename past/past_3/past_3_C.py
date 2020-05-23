A,R,N = map(int, input().split())
for i in range(N-1):
    if A > 10**9:
        print("large")
        exit()
    A *= R
if A > 10**9:
    print("large")
else:
    print(A)