A,B,m = gets.split.map(&:to_i)
a = gets.split.map(&:to_i)
b = gets.split.map(&:to_i)
min = 100000000
x = []
y = []
c = []
m.times do |i|
    x[i],y[i],c[i] = gets.split.map(&:to_i)
    if min >= a[x[i]-1]+b[y[i]-1]-c[i]
        min = a[x[i]-1]+b[y[i]-1]-c[i]
    end
end
if a.min+b.min < min
  min = a.min+b.min
end
puts min
