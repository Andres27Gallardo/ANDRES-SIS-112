import random      #se importa la libreria random
def geneList(lista_datos,rango,Vmin,Vmax):
    for i in range(rango):
        dato=random.randint(Vmin,Vmax)
        print(dato)
        lista_datos.append(dato)    
    return lista_datos

def encontrarNumero(lista,numero):
    for i in range(len(lista)):
        if(numero==lista[i]):
            print(f"numero encontrado en el indice: {i}")
            return 1