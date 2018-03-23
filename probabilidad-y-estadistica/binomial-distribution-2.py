from math import factorial,pow

# expected input 12 10
# expected output 0.891 0.342

# numbersStr = input().strip().split(' ')
# percentage = int(numbersStr[0])
# n = int(numbersStr[1])

percentage=12
n=10

p=percentage/100
def binomial(x,n,p):
    return (factorial(n)/(factorial(x)*factorial(n-x)))*pow(p,x)*pow((1-p),n-x)

value = 0
#de 0 hasta 2(inclusivo)
for x in range(0, 3):
    value = value + binomial(x,n,p)
print('{:.3f}'.format(value))

value = 0
#de 2 hasta n(inclusivo)
for x in range(2, n+1):
    value = value + binomial(x,n,p)
print('{:.3f}'.format(value))