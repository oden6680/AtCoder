import collections
N = int(input())
a = list(map(int, input().split()))
a = collections.Counter(a)
a_key = list(a.keys())
a_value = list(a.values())
cnt = 0
for i in range(len(a)):
    x = int(a_value[i])-int(a_key[i])
    if  x >= 0:
        cnt += x
    else:
        cnt += a_value[i]
print(cnt)