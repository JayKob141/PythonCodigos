
N=9
lineNumbers='3 7 8 5 12 14 21 13 18'
lineNumbers = lineNumbers.split(' ')
# Expected output
# 6
# 12
# 16

def median(data):
    print(data)
    N = len(data)
    if N%2 == 0:
        i = N//2   - 1
        value = data[i] + data[i + 1]
        value = value // 2
    else:
        i = (N+1)//2 - 1
        value = data[i]
    return value

# N = int(input())
# lineNumbers=input().strip().split(' ')

numbers = []
for strNumber in lineNumbers:
    numbers.append( int(strNumber) )
numbers.sort()

XMedian = median( numbers[0:len(numbers)] )
Notincluded = 0
Nhalf = N//2
if N%2 == 1:
    Nhalf = (N+1)//2
    Notincluded = 1

LMedian = median( numbers[0: Nhalf - Notincluded ])
UMedian = median( numbers[Nhalf : N ])

print(LMedian)
print(XMedian)
print(UMedian)


