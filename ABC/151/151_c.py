N,M = map(int, input().split())
pro_pen = [0]*N
pro_ac  = [0]*N
for i in range(M):
    p_i,s_i = map(str, input().split())
    if pro_ac[int(p_i)-1] == 0 and s_i == "WA":
        pro_pen[int(p_i)-1] += 1
    if pro_ac[int(p_i)-1] == 0 and s_i == "AC":
        pro_ac[int(p_i)-1] = 1
wa = 0
for i in range(N):
    if pro_ac[i] == 1:
        wa += pro_pen[i]
print(sum(pro_ac),wa)