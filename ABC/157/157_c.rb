n,m = gets.split.map(&:to_i)
s = []
c = []
m.times do |i|
    s[i],c[i] = gets.split.map(&:to_i)
end
result_f = Array.new(n)
result = Array.new(n)
for i in 0..(m-1)
    if result_f[s[i]-1] == 0
        result[s[i]-1] = c[i]
        result_f[s[i]-1] = 1
    else
        puts -1
        exit
    end
end
if n == 2
    if n[0] == nil
        n[0] = 1
    end
    if n[1] == nil
        n[1] = 0
    end
elsif n == 3
    if n[0] == nil
        n[0] = 1
    end
    if n[1] == nil
        n[1] = 0
    end
    if n[2] == nil
        n[2] = 0
    end
end
p result.join