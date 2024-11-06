import random
import time

lista_generado = []
lista_aletorio = []
lista = []

def menu():
    print("1. Ingresar n datos a lista")
    print("2. Generar lista aleatoria sin repetir")
    print("3. Ordenar la lista de menor a mayor")
    print("4. Búsqueda lineal")
    print("5. Búsqueda binaria")
    print("6. Descomporner un numero utilizando la recursividad")
    print("7. Salir ")
    
def ingresar_lista():
    try:
        numero_ingresar = int(input("Ingresa el número: "))
        if numero_ingresar in lista_generado:
            print("Este número ya existe en la lista.")
        else:
            lista_generado.append(numero_ingresar)
            print(f"Número {numero_ingresar} agregado a la lista.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
        
def generar_lista_aleatorio():
    try:
        numero_deseado = int(input("¿Cuántos números desea que tenga la lista?: "))
        numero_inicio = int(input("Seleccione el número inicial: "))
        numero_final = int(input("Seleccione el número final: "))
        
        for _ in range(numero_deseado):
            numero_random = random.randint(numero_inicio, numero_final)
            lista_aletorio.append(numero_random)
        
        print("Lista aleatoria generada:", lista_aletorio)
    except ValueError:
        print("Por favor, ingrese valores válidos.")
        
def ordenar_lista(lista):
    start_time = time.time()
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    end_time = time.time()
    print("Lista ordenada:", lista)
    print("Tiempo de ordenamiento:", end_time - start_time, "segundos")
    
def busqueda_lineal(lista, numero):
    start_time = time.time()
    for i in range(len(lista)):
        if lista[i] == numero:
            end_time = time.time()
            print(f"Número encontrado en la posición {i}")
            print("Tiempo de búsqueda lineal:", end_time - start_time, "segundos")
            return i
    end_time = time.time()
    print("Número no encontrado")
    print("Tiempo de búsqueda lineal:", end_time - start_time, "segundos")
    return -1
        

def busqueda_binaria(lista, numero):
    start_time = time.time()
    lista.sort()  # Asegurarse de que la lista esté ordenada
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == numero:
            end_time = time.time()
            print(f"Número encontrado en la posición {medio}")
            print("Tiempo de búsqueda binaria:", end_time - start_time, "segundos")
            return medio
        elif lista[medio] < numero:
            inicio = medio + 1
        else:
            fin = medio - 1
    end_time = time.time()
    print("Número no encontrado")
    print("Tiempo de búsqueda binaria:", end_time - start_time, "segundos")
    return -1


def descomponer_numero(numero=None):
    if numero is None:
        numero = int(input("Ingresa un número entero: "))
    if numero < 10:
        print([numero])
        return [numero]
    else:
        resultado = descomponer_numero(numero // 10) + [numero % 10]
        print(resultado)
        return resultado


