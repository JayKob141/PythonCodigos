from math import pow,exp,factorial,sqrt

x=0.88
y=1.55

avg_ca=160+40*(x + pow(x,2))
print( 'expected ca = {:.3f}'.format(avg_ca))
avg_cb=128+40*(y + pow(y,2))
print( 'expected cb = {:.3f}'.format(avg_cb))

# expected output
# 226.176
# 286.100