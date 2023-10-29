import math

def optimize(val, power):
    result = pow(val, power//2)
    result = result * result
    if power % 2 != 0:
        result = result * val
    return result

n = 4
b = [[0 for i in range(n)] for j in range(n)]

for i in range(0, n):
    for j in range(0, n):
        exp = 2023*(i+1)*(j+1)
        ans = (optimize(1669661,exp))%998244353
        b[j][i] = ans
        
for row in b:
    print (*row)
