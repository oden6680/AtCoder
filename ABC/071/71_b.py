S = list(input())
All = list("abcdefghijklmnopqrstuvwxyz")
res = list(set(S) ^ set(All))
if len(res) > 0:
    print(res[0])
else:
    print("None")
