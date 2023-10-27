n = 243
m = 998244353
solution_count = 0

for x in range(-n, n + 1):
    for y in range(-n, n + 1):
        z = (2 * y - 3 * x) / 6
        if abs(z) <= n and int(z) == z and x*y != 0:
            solution_count += 1
            
for x in range(-n, n + 1):
    for y in range(-n, n + 1):
        if x*y*(3*x-2*y)*(x-2*y) != 0:
            z = -2*(x**2-x*y)/(3*x-2*y)
            if abs(z) <= n and int(z) == z:
                solution_count += 1
                
print (solution_count)
