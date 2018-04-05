from math import pi,pow,sqrt, exp

two_over_sqrtpi = 2 / sqrt(pi)
dx = 0.00001
sqrt_2 = sqrt(2)
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

def cummulative(x,mean,std_d):
    z = (x - mean)/(std_d*sqrt_2)
    return (1/2)*(1 + erf( z ))

def normal_dist(x, mean, std_d):
    return ( 1 / (std_d * sqrt(2*pi)) ) * exp( - (pow(x - mean, 2)/(2*pow(std_d, 2))) )


value = cummulative(80, 70 , 10) - cummulative(70, 70 , 10)
resp1 = 0.5 - value
print('{:.2f}'.format(resp1 * 100))
print('{:.2f}'.format((0.5 + value)*100))
print('{:.2f}'.format(resp1 * 100))

# 15.87
# 84.13
# 15.87