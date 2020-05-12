a,b = map(str, input().split())
n = int(a+b)
i = 1
while n >= i**2:
    if n == i**2:
        print("Yes")
        exit()
    i += 1
print("No")