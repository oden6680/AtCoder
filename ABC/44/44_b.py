import collections
w = list(input())
c = collections.Counter(w)
c_value = list(c.values())
for i in range(len(c_value)):
    if c_value[i]%2:
        print("No")
        exit()
print("Yes")