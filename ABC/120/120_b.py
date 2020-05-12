A,B,K = map(int, input().split())
div_1 = []
div_res = []
for i in range(A+1):
    if i != 0 and A%i == 0:
        div_1.append(i)
for i in range(B+1):
    if i != 0 and B%i == 0 and (i in div_1):
        div_res.append(i)
div_res.reverse()
print(div_res[K-1])