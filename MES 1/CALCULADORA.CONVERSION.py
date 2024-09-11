import conversiones

def menuDeSeleccion():
    print("1. Metros a Kilomegros")
    print("2. Gramos a kilometros")
    print("3. Celsius a Fahrenheit")
    
print("-----Calculadora de conversion------ ")

menuDeSeleccion()
opcion = int(input("Selecione la opcion que desea realizar: "))
cantidad = float(input("Indica el valor de la unidad a convertir: "))

if opcion == 1:
    print(f"Resultado: {conversiones.MetroAKilometro(cantidad)}")
elif opcion == 2:
    print(f"Resultado: {conversiones.GramosAKilogramos(cantidad)}")
elif opcion == 3:
    print(f"Resultado: {conversiones.CelsiusAFahrenheit(cantidad)}")
else:
    print("No existe esta opción")
        

    
