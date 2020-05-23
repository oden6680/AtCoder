W = list(input())
boin = ["a","i","u","e","o"]
res = ""
for i in range(len(W)):
    if not W[i] in boin:
        res += W[i]
print("".join(res))