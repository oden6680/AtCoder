A = list(input())
S = [-1,1]
res = ["-","+"]
for i in range(2):
    for j in range(2):
        for k in range(2):
            if int(A[0])+int(A[1])*S[i]+int(A[2])*S[j]+int(A[3])*S[k] == 7:
                print(A[0]+res[i]+A[1]+res[j]+A[2]+res[k]+A[3]+"=7")
                exit()