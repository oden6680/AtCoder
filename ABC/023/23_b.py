N = int(input())
S = input()
res = "b"
for i in range(1,N+1):
    if res == S:
        print(i-1)
        exit()
    if i%3 == 1:
        res = "a"+res+"c"
    elif i%3 == 2:
        res = "c"+res+"a"
    else:
        res = "b"+res+"b"
print(-1)