s = list(input())
temp = s[0]
cnt = 0
A = []
for i in range(1,len(s)):
    if s[i] == temp[0]:
        temp += s[i]
        cnt += 1
    else:
        A.append(temp[0]+str(cnt+1))
        cnt = 0
        temp = s[i]
A.append(temp[0]+str(cnt+1))
print("".join(A))