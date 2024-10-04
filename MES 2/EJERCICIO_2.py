import random

lista = []

def geneLista (rango, minimo, maximo):
    for i in range (0, rango):
        numero = random.randint(minimo,maximo)
        lista.append(numero)
    print(lista)
    
rango = int(input("Hazta que rango quiere los numeros: "))
minimo = int(input("Desde que numero quiere que comienze a generar el numero aleatorio: "))
maximo = int(input("Hasta que numero quiere generar el numero aleatorio: "))

geneLista (rango, minimo, maximo)
