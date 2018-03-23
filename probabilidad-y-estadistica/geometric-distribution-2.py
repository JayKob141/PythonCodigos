from math import pow
p=1/3
n=5

def geometric_distribution(n,p):
    q = 1 - p
    return pow(q,n-1)*p

value = 0
for nthInspection in range(1 , n+1):
    value = value + geometric_distribution(nthInspection, p)
print('{:.3f}'.format(value))