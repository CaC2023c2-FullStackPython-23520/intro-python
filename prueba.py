num1=int(input("ingrese un numero: "))
if  num1==2 or num1==3 or num1==5 or num1==7:
    print("el numero", num1, "es primo")
elif num1%2==0 or num1%3==0 or num1%5==0 or num1%7==0:
    print("el numero", num1,"no es primo")
else:
    print("el numero", num1, "es primo")