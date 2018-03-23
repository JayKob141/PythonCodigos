# The probability that a machine produces a defective product is 1/3. 
# What is the probability that the 1st defect is found during the 5th inspection?
from math import pow
p=1/3
nthInspection=5

def geometric_distribution(n,p):
    q = 1 - p
    return pow(q,n-1)*p

value = geometric_distribution(nthInspection, p)
print('{:.3f}'.format(value))