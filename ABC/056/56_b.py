W,a,b = map(int, input().split())
print(max(0,max(a,b)-(W+min(a,b))))