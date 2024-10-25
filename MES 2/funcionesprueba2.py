lista_generado = []
lista_aletorio = []
import random
def menu():
    print("1. Ingresar la datos a lista")
    print("2. Generar lista aleatorio ")
    print("3. Ordenar la lista de menor a mayor ")
    print("4. Busqueda lineal")
    print("5. Busqueda binaria")

def Ingresar_lista():
    numero_ingresar = input(int("Ingresa el numero: "))
    if numero_ingresar in lista:
        print("Este numero ya existe dentro de la lista")
    else:
        lista_generado.append(numero_ingresar)
        

def generar_lista_aleatorio(n):
    numero_deseado= int(input("Cuantos numero desea que tenga su numero: "))
    numero_inicio= int(input("Selecione el numero que desea iniciar: "))
    numero_final = int(input("Seleccione el numero que desea finalizar: "))
    for i in range(0,numero_deseado):
        numeros_random = random.choices(numero_inicio,numero_final)
        lista_aleatorio.append(numeros_random)
    
def ordenar_lista(lista):
    

def busqueda_lineal(lista, numero):
    
    
def busqueda_binaria(lista,numero):
    
    
    