x = gets.chomp.to_i
cnt = 0
while x >= 500
    x -= 500
    cnt += 1000
end

while x >= 5
    x-= 5
    cnt += 5
end
puts cnt 