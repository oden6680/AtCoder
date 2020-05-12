n,x,y = gets.split.map(&:to_i)
a = gets.split.map(&:to_i)
cnt_x = 0
cnt_y = 1
x_a = []
y_a = []
(n/2).times do |i|
    x_a[i] = a[cnt_x]
    y_a[i] = a[cnt_y]
    cnt_x += 2
    cnt_y += 2
end
x_sum = x_a.inject(:+)+x
y_sum = y_a.inject(:+)+y
if y_sum == x_sum
    puts "Draw"
elsif y_sum > x_sum
    puts "Aoki"
else
    puts "Takahashi"
end
