"""
    El usuario ingresa su año de nacimiento. La máquina calcula
    y muestra su edad aproximada.
"""

# ENTRADA --> PROCESO --> SALIDA

anio_actual = 2023

# Entrada
anio_de_nacimiento = int(input("¿En qué año naciste? "))

# Proceso
edad = anio_actual - anio_de_nacimiento

# Salida
# Concatenar usando varios parámetros en el print()
print("Tu edad es de",edad,"ó",(edad-1),"años")
# Concatenar usando el + (solo para string)
print("Tu edad es de " + str(edad) + " ó " + str(edad-1) + " años")
# Concatenar con Interpolación de String
print(f"Tu edad es de {edad} ó {edad-1} años")