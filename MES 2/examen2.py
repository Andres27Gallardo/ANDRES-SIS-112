import funcionesexa2

while True:
    funcionesexa2.menu()
    x = input("Seleccione una opción: ")
    if x == "1":
        funcionesexa2.ingresar_lista()
    elif x == "2":
        funcionesexa2.generar_lista_aleatorio()
    elif x == "3":
        lista = funcionesexa2.lista_generado if int(input("¿Desea ordenar la lista generada (1) o la lista aleatoria (2)?: ")) == 1 else funcionesexa2.lista_aletorio
        funcionesexa2.ordenar_lista(lista)
    elif x == "4":
        numero = int(input("Ingrese el número a buscar: "))
        lista = funcionesexa2.lista_generado if int(input("¿Buscar en la lista generada (1) o en la lista aleatoria (2)?: ")) == 1 else funcionesexa2.lista_aletorio
        funcionesexa2.busqueda_lineal(lista, numero)
    elif x == "5":
        numero = int(input("Ingrese el número a buscar: "))
        lista = funcionesexa2.lista_generado if int(input("¿Buscar en la lista generada (1) o en la lista aleatoria (2)?: ")) == 1 else funcionesexa2.lista_aletorio
        funcionesexa2.busqueda_binaria(lista, numero)
    elif x == "6":
        funcionesexa2.descomponer_numero()
    elif x == "7":
        print("Saliendo del programa....")
        break
    else:
        print("Esa opción no es válida, ingrese otra opción.")