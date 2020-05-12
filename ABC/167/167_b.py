A,B,C,K = map(int, input().split())
cnt = 0
if A > K:
    print(K)
    exit()
if A+B >= K:
    print(A)
else :
    print(A-max(0,(K-A-B)))