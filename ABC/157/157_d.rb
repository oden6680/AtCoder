n,m,k = gets.split.map(&:to_i)
a = []
b = []
friend_c = Array.new(n-1)
friend = Array.new(n)
m.times do |i|
    a[i], b[i] = gets.split.map(&:to_i)
    if a[i]-b[i] == 1
        friend_c[b[i]-1] = 1
    elsif b[i]-a[i] == 1
        friend_c[a[i]-1] = 1
    end
end
c = []
d = []
k.times do |i|
    c[i], d[i] = gets.split.map(&:to_i)
    friend[c[i]-1] -= 1
    friend[d[i]-1] -= 1
end
