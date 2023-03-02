
import math
l=[]
for i in range(1,15):
    if i%2==0:
        l.append(i)
print(l)

res=(map(lambda n:math.sqrt(n),l))
print(list(res)) 
