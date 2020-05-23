s = input()
kenban = "WBWBWWBWBWBW"*3
ans = ['Do','Do','Re','Re','Mi','Fa','Fa','So','So','La','La','Si']
for i in range(12):
    if s == kenban[i:i+20]:
        print(ans[i])
        exit()