import math
m = 998244353
n = 10**6 + 2023
a = [None for i in range(n+1)]
a[0] = 2
a[1] = 1
sum = 0

for x in range(2, n):
    a[x] = (a[x-1] + a[x-2])%m

for i in range(0, math.ceil(n/3)):
    sum = sum + (((a[0+3*i])%m)**2)%m

print(sum%m)