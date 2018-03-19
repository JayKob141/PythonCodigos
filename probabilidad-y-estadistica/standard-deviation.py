from math import sqrt,pow
# N=int(input())
# numbersStr = input().strip().split(' ')

N=5
numbersStr = '10 40 30 50 20'.split(' ')
numbers = []

for number in numbersStr:
    numbers.append( int(number) )
suma = 0

for number in numbers:
    suma = suma + number

average = suma / N

suma2 = 0
for number in numbers:
    x = number - average
    suma2 = suma2 + pow(x,2) 

variance = suma2 / N
print( '{:.1f}'.format(sqrt(variance)))