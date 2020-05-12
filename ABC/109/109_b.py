N = int(input())
Word = []
tail = ""
for i in range(N):
    W = list(input())
    head = W[0]
    W = ''.join(W)
    if i != 0:
        if tail != head or (W in Word):
            print("No")
            exit()
    tail = W[-1]
    Word.append(W)
print("Yes")