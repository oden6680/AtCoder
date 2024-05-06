X ,Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)

apples = p[:X] + q[:Y] + r
apples.sort(reverse=True)
print(sum(apples[:X+Y]))