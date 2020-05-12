n, a, b = gets.split.map(&:to_i)
cnt = n/(a+b)
result = cnt*a
amari = n-(a+b)*cnt
if amari >= a
    result += a
else
    result += amari
end

puts result