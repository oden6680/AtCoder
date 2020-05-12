s = gets.chomp.to_chars
q = gets.chomp.to_i
query
q.times do
    query = gets.split(" ")
    if query[0] == '1'
        s = s.reverse
    elsif query[1] == '1'
        s = query[2]+s
    else
        s = s+query[2]
end
puts s