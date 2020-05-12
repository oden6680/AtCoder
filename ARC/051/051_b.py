K = int(input())
a = [1,1]
for i in range(40):
    a.append(a[-1] + a[-2])
print(a[K-1], a[K])