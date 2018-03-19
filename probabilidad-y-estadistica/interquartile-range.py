def median(data):
    N = len(data)
    if N%2 == 0:
        i = N//2   - 1
        value = data[i] + data[i + 1]
        value = value / 2
    else:
        i = (N+1)//2 - 1
        value = data[i]
    return value

def lineNumbersToArray(lineNumbers):
    N = len(lineNumbers)
    numbers = []
    for number in lineNumbers:
        numbers.append( int(number) )
    return numbers

def calculate_medians(numbers):
    N = len(numbers)
    XMedian = median( numbers[0:len(numbers)] )
    Notincluded = 0
    Nhalf = N//2
    if N%2 == 1:
        Nhalf = (N+1)//2
        Notincluded = 1
    LMedian = median( numbers[0: Nhalf - Notincluded ])
    UMedian = median( numbers[Nhalf : N ])
    return (LMedian, XMedian, UMedian)

    
# 6
# 6 12 8 10 20 16
# 5 4 3 2 1 5

# N = int(input())
# lineNumbers=input().strip().split(' ')
# inputNumbers = lineNumbersToArray(lineNumbers)
# lineNumbers=input().strip().split(' ')
# frequencies = lineNumbersToArray(lineNumbers)
N = 6
i = '6 12 8 10 20 16'
inputNumbers = i.split(' ')
inputNumbers = lineNumbersToArray(inputNumbers)
i = '5 4 3 2 1 5'
frequencies =  i.split(' ')
frequencies = lineNumbersToArray(frequencies)

# N = int(input())
# lineNumbers=input().strip().split(' ')
# inputNumbers = lineNumbersToArray(lineNumbers)
# lineNumbers=input().strip().split(' ')
# frequencies = lineNumbersToArray(lineNumbers)

numbers = [ ]
for i in range(0,N):
    for j in range(0, frequencies[i]):
        numbers.append( inputNumbers[i] )
numbers.sort()

medians = calculate_medians(numbers)
difference = medians[2] - medians[0]
print('{:.1f}'.format(difference))

