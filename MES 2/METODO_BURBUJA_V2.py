lista = [8,2,3,45,7,93,10,37,90,11]

for i in range(len(lista)):
    #print(f"INDCE = {i}     VALOR = {lista[i]}")
    for j in range(0,(len(lista)-i)):
        print(f"({lista[j]},{lista[j+1]})")
        if (lista[j]>lista[j+1]):
            lista[j],lista[j+1]=lista[j+1],lista[j]
            print(f"\n========================\nCambio({lista[j]},{lista[j+1]})\n============")
        