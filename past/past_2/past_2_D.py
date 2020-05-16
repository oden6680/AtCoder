S = list(input())
N = len(S)
cnt = min(3,N)+len(set(S))

unusing = set()
for i in range(N-1): #Pattern without using "." (length = 2)
    temp = S[i]+S[i+1]
    unusing.add(temp)
for i in range(N-2): #Pattern without using "." (length = 3)
    temp = S[i]+S[i+1]+S[i+2]
    unusing.add(temp)
cnt += len(unusing)

use_l = set()
for i in range(N-1):
    use_l.add(S[i+1])
for i in range(N-2):
    temp = S[i+1]+S[i+2]
    use_l.add(temp)
cnt += len(use_l)

use_center = set()
for i in range(1,N-1):
    use_center.add(S[i-1]+S[i+1])
cnt += len(use_center)

use_r = set()
for i in range(1,N):
    use_r.add(S[i-1])
for i in range(2,N):
    temp = S[i-2]+S[i-1]
    use_r.add(temp)
cnt += len(use_r)

use_l_2 = set()
for i in range(2,N):
    use_l_2.add(S[i])
cnt += len(use_l_2)

use_r_2 = set()
for i in range(N-2):
    use_r_2.add(S[i])
cnt += len(use_r_2)

use_wings = set()
for i in range(1,N-1):
    use_wings.add(S[i])
cnt += len(use_wings)

print(cnt)