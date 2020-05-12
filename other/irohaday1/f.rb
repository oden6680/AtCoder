require 'prime'
n,k = gets.split.map(&:to_i)
a = []
Prime.prime_division(n).each do |i,j|
  a += [i]*j
end
a = a.sort
if a.size < k
  puts -1
  exit
end
while a.size > k
  a[-2] *= a[-1]
  a.pop
end
puts a.join(' ')