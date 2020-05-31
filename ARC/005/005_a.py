N = int(input())
W = list(map(str, input().split()))
Word = ["TAKAHASHIKUN","Takahashikun","takahashikun","TAKAHASHIKUN.","Takahashikun.","takahashikun."]
cnt = 0
for i in range(N):
    if W[i] in Word:
        cnt += 1
print(cnt)