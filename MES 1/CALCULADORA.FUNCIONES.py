def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print("Seleccione la operación que desea realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicar")
print("4. Dividir")

c = int(input("¿Qué operación desea? "))

if c == 1:
    resultado = suma(a, b)
elif c == 2:
    resultado = resta(a, b)
elif c == 3:
    resultado = multiplicar(a, b)
elif c == 4:
    resultado = dividir(a, b)
else:
    print("Opción inválida")
    
print("El resultado es: ", resultado)