N = int(input())
N = N%30
res = ["1","2","3","4","5","6"]
for i in range(N):
    k = i%5
    temp = res[k]
    res[k] = res[k+1]
    res[k+1] = temp
print("".join(res))