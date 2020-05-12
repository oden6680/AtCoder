N = int(input())
original = N
S = 0
for i in range(len(str(N))):
    S += N%10
    N = N//10
if original%S == 0:
    print("Yes")
else:
    print("No")