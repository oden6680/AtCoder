S = list(input())
T = list(input())
for i in range(len(S)):
    if S[i] != T[i]:
        print("No")
        exit()
if len(T)-len(S) == 1:
    print("Yes")
else:
    print("No")