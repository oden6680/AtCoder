def function(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1
s = int(input())
a = []
a.append(s)
i = 0
while len(a) == len((set(a))):
    a.append(function(a[i]))
    i += 1
print(i+1)