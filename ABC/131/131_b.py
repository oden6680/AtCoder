n,l = map(int, input().split())
base_taste = n*l+(n*n-n)//2
if l > 0:
    print(base_taste-l)
elif n+l >= 1:
    print(base_taste)
else:
    print(base_taste-l-n+1)