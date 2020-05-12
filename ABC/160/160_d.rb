n,x,y = gets.split.map(&:to_i)
elipse = y-x+1
k = 1
(n-1).times do 
    if k == 1
        puts n
    elsif elipse*1.0/2 > k
        puts n+