N = int(input())
A = list(map(int, input().split()))
cnt_0 = A.count(0)
SUM = sum(A)
div = N-cnt_0
if SUM%div == 0:
    print(SUM//div)
else:
    print(SUM//div+1)