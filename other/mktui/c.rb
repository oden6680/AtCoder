A,B,C = gets.split.map(&:to_i)
if a+b+2*Math.sqrt(a*b) < c 
    puts "Yes"
else 
    puts "No"
end
n = 1
while n < 10**9
    n += 1
    
    n = n*n