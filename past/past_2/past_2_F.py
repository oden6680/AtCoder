N = int(input())
tasks_point = [0]*N
for i in range(N):
    a,b = map(int, input().split())
    if tasks_point[a-1] < b:
        tasks_point[a-1] = b
for i in range(N):
    print(sum(tasks_point[0:i]))