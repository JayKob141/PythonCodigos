
N=int(input())
strValues=input().strip().split(' ')
strWeights=input().strip().split(' ')
sumsValues=0
sumsWeights=0
for i in range(0,N):
    value = int(strValues[i])
    weight = int(strWeights[i])
    sumsValues = sumsValues + weight * value
    sumsWeights = sumsWeights + weight
print('{:.1f}'.format(sumsValues/sumsWeights))
