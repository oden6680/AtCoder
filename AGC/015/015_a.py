N,A,B = map(int, input().split())
if A > B or (A != B and N == 1):
    print(0)
else:
    N -= 2
    print(N*(B-A)+1)