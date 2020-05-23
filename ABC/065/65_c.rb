n,m = gets.split.map(&:to_i)
mod = 10**9+7
if (n-m).abs > 1
    puts 0
    exit
end
def factorial(x)
    (1..x).inject{|sum, i| (sum * i) % mod}
  end
a = [n,m]
if n != m
    puts (factorial(a.max)**2/a.max)%mod
else
    puts 2*(factorial(a.max)**2)%mod
end