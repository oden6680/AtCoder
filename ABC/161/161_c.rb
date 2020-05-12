n,k = gets.split.map(&:to_i)
if n >= k 
    n = n%k
end
if n == 0
    puts 0
    exit
end
while (k/n) != 1
    n = k-n
end
puts k-n