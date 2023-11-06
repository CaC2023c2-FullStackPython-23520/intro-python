def cambiar(un_color):
    un_color = "Verde"
    return un_color

def quitar1(lista):
    lista.pop()
    return lista

# Programa principal
color = "Rojo"
print(color) # Rojo
cambiar(color)
print(color) # Rojo

pares = [2, 4, 6, 8]
print(pares) # 2,4,6,8
quitar1(pares)
print(pares) # 2,4,6