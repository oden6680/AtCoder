X = list(map(int, input().split()))
midle = sum(X)-min(X)-max(X)
dif_1 = max(X)-midle
new_min = min(X)+dif_1
dif_2 = max(X)-new_min
if dif_2%2 == 0:
    print(dif_1+dif_2//2)
else:
    print(dif_1+(dif_2//2)+2)