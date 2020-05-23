A,B,C,K = map(int, input().split())
if (abs(A-C) <= K) or (abs(A-B) <= K and abs(B-C) <= K):
    print("Yes")
else:
    print("No")