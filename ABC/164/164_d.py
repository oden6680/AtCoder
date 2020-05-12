S = input()
n = len(S)
cnt = 0
x = range(2019, int(S), 2019)
for i in range(len(x)):
    cnt += S.count(str(x[i]))
print(cnt)