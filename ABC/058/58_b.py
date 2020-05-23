O = list(input())
E = list(input())
S = ""
for i in range(len(O)):
    S += O[i]
    if i < len(E):
        S += E[i]
print(S)