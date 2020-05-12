def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table
X = int(input())
div = divisor(X)
div.sort()
n = len(div)
for i in range(n):
    print(i)
    if X < 0:
        a = 0
        b = div[i]
        while a**5 - (b**5) != X or a**5 - (b**5) > X:
            a = a-1
            b += 1
    else:
        a = div[i]
        b = 0
        while a**5 - (b**5) != X or a**5 - (b**5) < X:
            a += 1
            b = b-1
print(a,b)