N,T = map(int, input().split())
min_cost = 10**9
for i in range(N):
    c,t = map(int, input().split())
    if T >= t and min_cost > c:
        min_cost = c
if min_cost == 10**9:
    print("TLE")
    exit()
print(min_cost)