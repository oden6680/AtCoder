import collections
N = int(input())
a = list(map(int, input().split()))
if N == 1:
    print(1)
    exit()
if N == 2:
    if abs(a[0]-a[1]) <= 2:
        print(2)
    else:
        print(1)
    exit()
c = collections.Counter(a)
c_key = list(c.keys())
c_value = list(c.values())
res = 0
if len(c) == 2:
    if int(c_key[1])-int(c_key[0]) <= 2:
        print(c_value[0]+c_value[1])
        exit()
for i in range(1,len(c)-1):
    temp = c_value[i]
    temp_2 = 0
    temp_3 = 0
    flag = True
    if int(c_key[i])-int(c_key[i-1]) == 1:
        temp += c_value[i-1]
        flag = False
    if int(c_key[i+1])-int(c_key[i]) == 1:
        temp += c_value[i+1]
        flag = False
    if flag and int(c_key[i+1])-int(c_key[i]) == 2:
        temp_2 = c_value[i+1]+c_value[i]
        flag = False
    if flag and int(c_key[i])-int(c_key[i-1]) == 2:
        temp_3 = c_value[i-1]+c_value[i]
    if max(temp,temp_2,temp_3) > res:
        res = max(temp,temp_2,temp_3)
print(max(res,c_value[0],c_value[-1]))
