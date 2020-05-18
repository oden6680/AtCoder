K = int(input())
S = input()
n = len(S)
if n <= K:
    print(S)
else:
    print(S[:K]+"...")