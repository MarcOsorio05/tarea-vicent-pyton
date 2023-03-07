# Inicializamos la variable de la suma en cero.
suma = 0

# Usamos un bucle for para iterar sobre todos los números menores que 100.
for num in range(2, 100):
    # Verificamos si el número es primo o no.
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    
    # Si el número es primo, lo agregamos a la variable de suma.
    if es_primo:
        suma += num

# Imprimimos el resultado de la suma.
print("La suma de todos los números primos menores que 100 es:", suma)
