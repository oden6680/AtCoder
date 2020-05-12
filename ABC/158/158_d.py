S = input()
Q = int(input())
flag = 0   #"1" represents inversion
head = ""
tail = ""
for i in range(Q):
    quary = list(map(str, input().split()))
    if quary[0] == "1":
        if flag == 0:
            flag = 1
        else:
            flag = 0
    else:
        if flag == 1:
            if quary[1] == "1":
                tail = tail+quary[2]
            else:
                head = quary[2]+head
        else:
            if quary[1] == "1":
                head = quary[2]+head
            else:
                tail = tail+quary[2]
S = head+S+tail
if flag == 1:
    S = S[::-1]
print(S)