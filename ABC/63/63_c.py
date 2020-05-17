N = int(input())
a = []
not_ten = []
for i in range(N):
    k = int(input())
    a.append(k)
    if k%10 != 0:
        not_ten.append(k)

a = sorted(a)
not_ten = sorted(not_ten)
res = sum(a)
if res%10 != 0:
    print(res)
elif len(not_ten) > 0:
    print(res-not_ten[0])
else:
    print(0)