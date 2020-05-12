from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
val = list(cnt.values())
s = 0
for i in val:
  s += i*(i-1)//2
for i in A:
  print(s-(cnt[i]-1))