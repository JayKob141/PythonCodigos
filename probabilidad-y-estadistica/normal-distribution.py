from math import pi,pow,sqrt, exp
# mean and standard deviation for X
# mean = 20 
# std_deviation = 2
upper_bound_A = 19.5

lower_bound_B = 20 
upper_bound_B = 22


two_over_sqrtpi = 2 / sqrt(pi)

dx = 0.00001
def summation(z):
    x= 0
    area = 0
    while x < z:
        y = exp(-pow( x ,2))
        area += dx * y 
        x += dx
    return area

def erf(z):
    return two_over_sqrtpi * summation(z)

sqrt_2 = sqrt(2)
def cummulative(x,mean,std_d):
    z = (x - mean)/(std_d*sqrt_2)
    return (1/2)*(1 + erf( z ))

def normal_dist(x, mean, std_d):
    return ( 1 / (std_d * sqrt(2*pi)) ) * exp( - (pow(x - mean, 2)/(2*pow(std_d, 2))) )

upper_bound_A = 20 + 20 - upper_bound_A 
resp1 = cummulative(upper_bound_A, 20, 2) - cummulative(20, 20, 2) 
resp1 = 0.5 - resp1
resp2 = cummulative(upper_bound_B, 20, 2) - cummulative(lower_bound_B, 20, 2) 

print('{:.3f}'.format(resp1))
print('{:.3f}'.format(resp2))


