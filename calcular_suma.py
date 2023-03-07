# Inicializamos la variable de la suma en cero.
suma = 0

# Usamos un bucle for para sumar los términos de la expresión.
for i in range(20, 100):
    termino = (2 * i + 1) ** 2 - (2 * i - 1) ** 2
    suma += termino

# Imprimimos el resultado de la suma.
print("La suma de la expresión es:", suma)
