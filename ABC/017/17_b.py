s = list(input())
res = ""
for i in range(len(s)):
    if s[i] == "c":
        res += "ch"
    elif s[i] == "o":
        res += "o"
    elif s[i] == "k":
        res += "k"
    elif s[i] == "u":
        res += "u"
if res == ''.join(s):
    print("YES")
else:
    print("NO")