n = gets.chomp.to_i
a = []
n.times do |i|
    a|i| = gets.chomp.to_i
end
k = 0
cnt = 0
while k != 1
    cnt += 1
    k = a[k]-1
    if cnt > n
        break
    end
end
if cnt <= n
    puts cnt
else
    puts -1
end