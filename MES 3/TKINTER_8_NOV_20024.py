import tkinter as tk
import csv  #Para crear el archivo que guardara el contacto
#Siempre para agragar a la ventana tiene que ser con el nombre  de la variable.pack

ventana = tk.Tk()
ventana.title("Nombre de la ventana ")
ventana.geometry("900x700") #Primer numero el ancho y el segundo el alto

nombre_contacto = tk.Label(ventana, text="Nombre") #Variable , Llammar a al la ventana, tect = es para mostrar en al ventana
nombre_contacto.pack() # Poner la variable, agregar a la ventana creada, el pack ira en el orden que esta en el codigo 
entrada_nombre=tk.Entry(ventana) #Para ingresar texto
entrada_nombre.pack() 

entrada_telefono = tk.Label(ventana, text="ingrese el telefono o celular")
entrada_telefono.pack()
entrada_telefono=tk.Entry(ventana)
entrada_telefono.pack()

entrada_edad = tk.Label(ventana, text="Ingrese su edad")
entrada_edad.pack()
entrada_edad=tk.Entry(ventana)
entrada_edad.pack()

entrada_correo = tk.Label(ventana, text="Ingrese su correo")
entrada_correo.pack()
entrada_correo=tk.Entry(ventana)
entrada_correo.pack()

def guardar():
    nombre=entrada_nombre.get() #get para extraer lo que estaba escrito en el cuadro de texto, almacena en nombre
    telefono=entrada_telefono.get()
    edad=entrada_edad.get()
    correo=entrada_correo.get()
    with open("agenda.csv","a",newline="")as archivo:#Para abrir un archivo
        contacto=csv.writer(archivo) 
        contacto.writerow([nombre,telefono,edad,correo])#Es para que trabaje en columna
    
boton_guardar=tk.Button(ventana, text="Guardar contacto", command=guardar)#command es para que realize una funcion, que se desigana
boton_guardar.pack()

ventana.mainloop()

