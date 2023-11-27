from super_matematica import factorial

try:
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    print(f"{a} / {b} es {a/b}")
    print(f"{a}! -> {factorial(a)}")
    print(f"{b}! -> {factorial(b)}")
    print("Todo salió bien")
except ValueError as e:
    print("Se ingresó cadena donde se espera entero")
except ZeroDivisionError as e:
    print("Se intentó dividir por cero")
#except ArithmeticError as e:
    #print(e)
#except Exception as e:
    #print("Ocurrió algún error...")

# ValueError cuando se ingresa cadena donde se espera entero
# ZeroDivisionError: Cuando se intenta dividir por b siendo cero