a,b = gets.split.map(&:to_i)
res_10 = []
res_8 = []
cnt = 0
for i in 0..1000
    if (i*0.08).to_i == a
        res_8[cnt] =  i
        cnt += 1
    end
end
cnt = 0
for i in 0..1000
    if (i*0.1).to_i == b
        res_10[cnt] =  i
        cnt += 1
        break
    end
end
result = []
result = res_10 && res_8
if result >= 0
    puts result[0]
else
    puts -1
end