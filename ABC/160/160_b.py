X = int(input())

happy = (X // 500) * 1000
X = X - (X // 500) * 500
happy += (X // 5) * 5

print(happy)