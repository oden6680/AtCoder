n,a,b = gets.split.map(&:to_i)
d = []
d = gets.split.map(&:to_i)
d = d.sort.unshift(0).push(n+1)
result = 0
for i in 0..(b+1)
    x = d[i+1]-(d[i]+1)
    result = x + x/a
end
puts result