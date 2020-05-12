N = int(input())
L = list(map(int, input().split()))
most = max(L)
if 2*most < sum(L):
    print("Yes")
else:
    print("No")