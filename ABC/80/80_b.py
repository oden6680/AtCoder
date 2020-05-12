N = int(input())
x = N
sums = 0
while x > 0:
    sums += x%10
    x = x//10
if N%sums == 0:
    print("Yes")
else:
    print("No")