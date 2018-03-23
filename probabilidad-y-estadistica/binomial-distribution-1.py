#expected input 1.09 1
#expected output 0.696

from math import factorial,pow
# numbersStr = input().split(' ').strip()
n = 6
#1.09
# xBoys = int(numbersStr[0])
xBoys = 1.09
#1.0
#xGirls = int(numbersStr[1])
xGirls = 1.0

#p=1.0 - (xGirls/xBoys)
p=xBoys/(xBoys+xGirls)
# p=1/xBoys
# p = 1 -( 1 / xBoys / 2 )
# print(p)

def binomial(x,n,p):
    return (factorial(n)/(factorial(x)*factorial(n-x)))*pow(p,x)*pow((1-p),n-x)

value = 0
#de 3 hasta 6
for x in range(3, 7):
    value = value + binomial(x,n,p)
print('{:.3f}'.format(value))