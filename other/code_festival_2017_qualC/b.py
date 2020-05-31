N = int(input())
A = list(map(int, input().split()))
res = 3**N
odd_cnt = 0
for i in A:
    if i%2 == 0:
        odd_cnt += 1
print(res - 2**odd_cnt)