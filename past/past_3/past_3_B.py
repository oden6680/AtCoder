N,M,Q = map(int, input().split())
get_point = [0]*N
problem_point = [0]*M
solve_cnt = [0]*M
solve_list = [0]
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(get_point[query[1]-1])
    else:
