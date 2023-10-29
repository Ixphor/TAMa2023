import math
import numpy as np

def optimize(val, power):
    result = pow(val, power//2)
    result = result * result
    if power % 2 != 0:
        result = result * val
    return result

n = 8
m = 998244353
b = [[0 for i in range(n)] for j in range(n)]
a = [0 for i in range(n**2)]
sum = 0

for i in range(0, n):
    for j in range(0, n):
        exp = 2023*(i+1)*(j+1)
        ans = (optimize(1669661,exp))%m
        b[j][i] = ans
        a[n*j + i] = ans
        
for row in b:
    print (*row)

a.sort(reverse=False)

aa = 149369469*15
ba = 149369469*15
ab = 149369469*15
ca = 149369469*3 + 264760536*12
ac = 149369469*3 + 264760536*12
da = 149369469*3 + 264760536*2 + 395914482*10
db = 149369469*3 + 264760536*2 + 395914482*10
ad = 149369469*3 + 264760536*2 + 395914482*10
bd = 149369469*3 + 264760536*2 + 395914482*10
bb = 149369469*3 + 264760536*2 + 395914482*4 + 457144271*3 + 444183063*3
cb = 149369469*3 + 264760536*2 + 395914482*4 + 457144271*3 + 444183063*3
bc = 149369469*3 + 264760536*2 + 395914482*4 + 457144271*3 + 444183063*3
cc = 149369469*3 + 264760536*2 + 395914482*4 + 457144271*3 + 444183063*3
dc = 149369469*3 + 444183063*6 + 395914482*4 + 264760536*2
cd = 149369469*3 + 444183063*6 + 395914482*4 + 264760536*2
dd = 149369469*3 + 444183063*6 + 395914482*4 + 264760536*2
answer = (aa + ab + ac +ad + ba + bb + bc +bd+ca+cb+cc+cd+da+db+dc+dd)
print(answer%m)

'''mincount = a.count(a[0])
sum = a[0]*(n**2-1)*mincount
print(sum)

for i in range(len(a)):
    for j in range (len(a)):
        if i == 0 and j == 0 or i == (n-1) and j == (n-1):
            if b[i+1][j] == a[0] or b[i-1][j] == a[0]:
                sum += b[i+1][j]*15'''
                
