import sys
sys.setrecursionlimit(2000)
def factorial_iterativo(n):
    resultado=1
    for i in range(1, n+1):
        resultado *= i
        print(f"Paso {i}: resultado = {resultado}")
    return resultado
def factorial(n):
    if n==0:
        return 1
    else:
        print(n)
        return n*factorial(n-1)
numero=5
print(factorial(numero))