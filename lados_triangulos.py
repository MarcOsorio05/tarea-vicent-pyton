import math

# Pedimos los tres lados del triángulo
a = float(input("Ingrese la longitud del primer lado: "))
b = float(input("Ingrese la longitud del segundo lado: "))
c = float(input("Ingrese la longitud del tercer lado: "))

# Calculamos el semiperímetro del triángulo
s = (a + b + c) / 2

# Calculamos el área del triángulo usando la fórmula de Herón
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Imprimimos el resultado
print("El área del triángulo es:", area)

