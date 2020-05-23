s = list(input())
t = list(input())
if s == t:
    print("same")
    exit()
for i in range(len(s)):
    if not (s[i].upper() == t[i] or s[i].lower() == t[i]):
        print("different")
        exit()
print("case-insensitive")