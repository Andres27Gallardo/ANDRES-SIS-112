#Argumento ("argumetnos")
def menu():
    print("""===SISTEMA \nDE NOTAS===
        1. Agregar nota
        2. Eliminar nota
        3. Modificar nota
        4. Mostrar todas las notas
        5. Calcular promedio
        6. Obtener nota máxima y mínima
        7. Salir""")
def add_nota(lista):
    a = int(input("INgrese la nota: "))
    lista.append(a)   
    return lista
def del_notas(lista):
    ind=len(lista)
    a = int(input("Ingrese un indice: "))
    lista.pop(a)
    return lista
def mod_nota(lista):
    a = int(input("Ingrese el indice a modificar"))
    b=float(input(f"Ingrse el numero a modificar de la lista {lista(a)}"))
    lista[a]=b
    return lista
def m_notas(lista):
    print("Las notas son: ", lista)
    return lista
def cal_promedio(lista):
    a = sum(lista)/len(lista)
    return a
def max_min_notas(lista):
    max = max(lista)
    min = min(lista)
    return max, min