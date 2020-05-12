n = int(input())
c = input()
w = ['A','B','X','Y']
ans = 10**9
for ll in w:
    for lr in w:
        for rl in w:
            for rr in w:
                l = ll+lr
                r = rl+rr
                res = c.replace(l,'L')
                res = res.replace(r,'R')
                ans = min(len(res),ans)
print(ans)