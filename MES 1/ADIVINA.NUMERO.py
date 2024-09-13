import random
print("Bienvenido a ADIVINA EL NUMERO")
print("El numero buscado es de 0 al 10")

numeroAle = random.randint(0,10)

contador = 0

while True:
    numeroUsu= int(input("Seleccione un numero: "))
    contador = contador+1
    if numeroUsu < numeroAle:
        print("Demasiado bajo, intente de nuevo")
    elif numeroUsu > numeroAle:
        print("Demasiado alto, intente de nuevo")
    elif numeroUsu == numeroAle:
        print("---------------")
        print("¡¡¡¡¡Felicidades!!!!")
        break
    
        
print("El numero de intentos es: ",contador)
print("----------------")