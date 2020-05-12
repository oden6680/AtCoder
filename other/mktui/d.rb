n = gets.to_i

def f(n, m, k, s)
  if n == m
    puts s.join.tr!("0-9", "a-z")
  else
    (0...k).each { |i| f(n, m + 1, k, s << i) }
    f(n, m + 1, k + 1, s << k)
  end
  s.pop
end

f(n, 0, 0, [])
