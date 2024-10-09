import funcioneseje3 as tarea
import time

lista=[]
rang=int(input("Dame el numero de elementos de la lista: "))
Vmin=int(input("Dame el valor minimo que debe tener: "))
Vmax=int(input("Dame el valor maximo que debe tener: "))
inicio=time.time()
tarea.generarLista(rang, Vmin, Vmax, lista)
fin=time.time()


print(f"la lista resultante es: {lista}")
print(f"numero de componentes: {len(lista)}")
print(type(lista))
x=sorted(lista)
num=int(input("Ingrese el numero que desea encontrar: "))
ini2=time.time()
tarea.encontrarNumero(lista, num)
fin2=time.time()

print(x)
ini3=time.time()
tarea.busqueda_binaria(x, num)
fin3=time.time()

print(f"el tiempo transcurrdio de la generacion de la lista \n {(fin-inicio)*1000} ms")
print(f"el tiempo transcurrdio de la busqueda lineal fue: \n {(fin2-ini2)*1000} ms")
print(f"el tiempo transcurrdio de la busqueda binaria fue: \n {(fin3-ini3)*1000} ms")