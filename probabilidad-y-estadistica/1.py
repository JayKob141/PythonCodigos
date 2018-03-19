
# file = open('./data-2.txt')
# N = int( file.readline().strip() )
# lineNumbers = file.readline()
# file.close()

N=int(input())
lineNumbers=input()

Numbers=lineNumbers.split(' ')

occurrences={}
numeros=[]
suma = 0
for i in range(0,N):
    numberStr = Numbers[i]
    number = int(numberStr.strip())
    suma = suma + number
    numeros.append( number )
    
    try:
        occurrences[numberStr] = occurrences[numberStr] + 1      
    except KeyError:
        occurrences[numberStr] = 1

modeStr = ''
for key,value in occurrences.items():
    if len(modeStr) == 0:
        modeStr = key
    elif occurrences[modeStr] < occurrences[key]:
        modeStr = key
    elif occurrences[modeStr] == occurrences[key]:
        a = int(modeStr)
        b = int(key)
        c = min(a,b)
        modeStr = str(c)




# Mean o promedio
numeros.sort()
# print(numeros)
# print('Total de numeros =',len(numeros))
print( '{:.1f}'.format(suma/N) )

# Mediana
if (N % 2) == 0:
    i = N//2        - 1
    value = numeros[i] + numeros[i + 1]
    value2 = value / 2
    print( value2 )
else:
    #es impar
    i = (N + 1)//2    - 1
    print( numeros[i] )

# Moda
print(modeStr)

