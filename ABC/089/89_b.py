N = int(input())
S = map(str, input().split())
if len(set(S)) == 3:
    print("Three")
else:
    print("Four")