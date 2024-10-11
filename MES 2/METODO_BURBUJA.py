def ordenamiento_burbuja(lista):
    n = len(lista)
    #Recoge toda la lista
    for i in range(n):
        #Ultios i elementosya estan ordenados
        for j in range(0,n-i - 1):
            #Intercambia si el elemnto actual es mayor que el siguiente
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1]= lista[j+1],lista[j]
    return lista

#Ejemplo de uso 
lista = [5,3,8,4,2,1]
print("lista original: ", lista)
lista_ordenada = ordenamiento_burbuja(lista)
print("lista ordenada: ", lista_ordenada)