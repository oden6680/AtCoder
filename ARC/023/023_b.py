R,C,D = map(int, input().split())
A = []
for _ in range(R):
	A.append(list(map(int,input().split())))
res = 0
for i in range(R):
	for j in range(C):
		if i+j<= D and (D-(i+j))%2 == 0:
			res = max(res,A[i][j])
print(res)