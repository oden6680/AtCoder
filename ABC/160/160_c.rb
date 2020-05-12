k,n = gets.split.map(&:to_i)
a = gets.split.map(&:to_i)
a.delete(0).sort
if a.max > a.min + k/2
    puts k - (a.max-a.min)
else
    puts a.max - a.min
end