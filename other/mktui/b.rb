w,h = gets.split.map(&:to_i)
if (W*h)%2 == 0
    puts (w*h)/2
else
    puts (w*h+1)/2
end
