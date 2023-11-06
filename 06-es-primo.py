# Definición de funciones
def es_multiplo(a, b):
    return a % b == 0

def cant_divisores(n):
    cant = 1
    for i in range(2,n+1):
        if es_multiplo(n, i):
            cant += 1
    return cant

def es_primo(n):
    return cant_divisores(n) == 2

# Programa principal
numero = int(input("Ingrese un número: "))
print(f"El {numero} ", end="")
if not es_primo(numero):
    print("NO ", end="")
print("es primo")