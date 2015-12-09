# print pi to the 5th decimal
# given pi = 4(1/1-1/3+1/5-1/7...)
pseudo_pi = 1
sum_fract = 0
bottom = 1.0
sign = 1
while round(pseudo_pi,5) is not 3.14159:
    sum_fract += sign / bottom
    bottom += 2
    sign *= -1
    pseudo_pi = 4 * sum_fract
    print pseudo_pi, bottom    
    
    
