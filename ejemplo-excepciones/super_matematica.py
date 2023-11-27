def factorial(n):
    if n < 0:
        raise ArithmeticError(f"No se puede hacer el factorial de {n}")
    f = 1
    for i in range(2, n+1):
        f *= i
    return f