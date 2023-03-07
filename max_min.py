import random

# Inicializamos las variables max_num y min_num con el valor inicial
# para que podamos comparar y encontrar el número máximo y mínimo.
max_num = 0
min_num = 999

# Usamos un bucle for para generar 100 números aleatorios de tres dígitos.
for i in range(100):
    num = random.randint(100, 999)
    
    # Comparamos el número generado con los valores actuales de max_num y min_num
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Imprimimos el número máximo y mínimo.
print("El número máximo es:", max_num)
print("El número mínimo es:", min_num)


