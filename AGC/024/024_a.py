A,B,C,K = map(int, input().split())
MAX = 10**18
if abs(A-B) > MAX:
    print("Unfair")
elif K%2:
    print(B-A)
else:
    print(A-B)