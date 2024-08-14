

x = int(input("Seleccione el primer número que desea ingresar: "))
y = int(input("Seleccione el segundo número que desea ingresar: "))

print("1. Suma/ 2. Resta/ 3. Multiplicar/ 4. Dividir")
z = int(input("Seleccione la operación que desea realizar: "))

if z == 1:
    resultado = x + y
elif z == 2:
    resultado = x - y
elif z == 3:
    resultado = x * y
elif z == 4:
    resultado = x / y
    
print("El resultado es: ", resultado)
