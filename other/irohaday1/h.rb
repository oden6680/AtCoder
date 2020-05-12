def f(n)
  answer = 0
  while n > 0
    answer += n%10
    n /= 10
  end
  return answer
end
n = gets.chomp.to_i
x = f(n)
result = []
while x >= 9
  result << 9
  x -= 9
end
if x > 0
  result = result.insert(0,x)
end
if result.join.to_i == n
  if result[0] == 9
    result[0] -= 1
    result = result.insert(0,1)
  elsif result.size >= 2
    result[0] += 1
    result[1] -= 1
  else
    result[0] -= 1
    result = result.insert(0,1)
  end
end

puts result.join
