s = list(input())
Max = 0
cnt = 0
D = ["A","C","G","T"]
for i in s:
    if i in D:
        cnt += 1
    else:
        if Max < cnt:
            Max = cnt
        cnt = 0
print(max(Max,cnt))