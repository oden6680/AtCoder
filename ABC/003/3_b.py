S = list(input())
T = list(input())
AtCoder = ["a","t","c","o","d","e","r"]
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif (S[i] == "@" and (not T[i] in AtCoder)) or (T[i] == "@" and (not S[i] in AtCoder)) or (S[i] != "@" and T[i] != "@"):
        print("You will lose")
        exit()
print("You can win")