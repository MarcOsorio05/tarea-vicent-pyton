import math

def taylor_exp(x, n):
    # Calcula la aproximación de e^x utilizando el polinomio de Taylor de grado n
    approx = 0
    for i in range(n):
        approx += (x**i) / math.factorial(i)
    return approx

e_approx = taylor_exp(5, 9)
e_exact = math.exp(5)

print("Aproximación de e^5:", e_approx)
print("Valor exacto de e^5:", e_exact)
