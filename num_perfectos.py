# Inicializamos las variables necesarias.
num = 2
cont = 0

# Usamos un bucle while para buscar los números perfectos.
while cont < 4:
    suma_divisores = 1  # Inicializamos en 1 porque todo número es divisible por 1.
    for i in range(2, num):
        if num % i == 0:
            suma_divisores += i
    
    if suma_divisores == num:
        # Si encontramos un número perfecto, lo imprimimos y aumentamos el contador.
        print(num, "es un número perfecto.")
        cont += 1
    
    num += 1  # Incrementamos el número para seguir buscando.

