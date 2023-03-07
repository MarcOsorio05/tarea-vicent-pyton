import math

def approx_e():
    sum = 0
    for k in range(9):
        sum += (5 ** k) / math.factorial(k)
    return sum

print(approx_e())
