N,A,B = map(int, input().split())
res = 0
for i in range(N):
    s,d = map(str, input().split())
    if s == "West":
        if int(d) < A:
            res -= A
        elif A <= int(d) <= B:
            res -= int(d)
        else:
            res -= B
    else:
        if int(d) < A:
            res += A
        elif A <= int(d) <= B:
            res += int(d)
        else:
            res += B
if res > 0:
    print("East", res)
elif res == 0:
    print(0)
else:
    print("West", abs(res))