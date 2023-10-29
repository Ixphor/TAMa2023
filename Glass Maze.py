import math
import numpy as np

def optimize(val, power):
    result = pow(val, power//2)
    result = result * result
    if power % 2 != 0:
        result = result * val
    return result

n = 4
b = [[0 for i in range(n)] for j in range(n)]
a = [0 for i in range(n**2)]
sum = 0

for i in range(0, n):
    for j in range(0, n):
        exp = 2023*(i+1)*(j+1)
        ans = (optimize(1669661,exp))%998244353
        b[j][i] = ans
        a[4*j + i] = ans
        
for row in b:
    print (*row)
    
a.sort(reverse=False)

mincount = a.count(a[0])
sum = a[0]*(n**2-1)*mincount

print(sum)
