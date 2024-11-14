
import tkinter as tk

ventana = tk.Tk()
ventana.title("CALCULADORA-ANDRES")
ventana.geometry("300x400") 

mensaje =tk.Label(ventana, text="Solo operaciones de dos variables ")
mensaje.pack()


boton_1 = tk.Button(ventana, text="1", width=5, height=2)
boton_1.place(x=20, y=220)

boton_2 = tk.Button(ventana, text="2", width=5, height=2)
boton_2.place(x=90, y=220)

boton_3 = tk.Button(ventana, text="3", width=5, height=2)
boton_3.place(x=160, y=220)

boton_4 = tk.Button(ventana, text="4", width=5, height=2)
boton_4.place(x=20, y=150)

boton_5 = tk.Button(ventana, text="5", width=5, height=2)
boton_5.place(x=90, y=150)

boton_6 = tk.Button(ventana, text="6", width=5, height=2)
boton_6.place(x=160, y=150)

boton_7 = tk.Button(ventana, text="7", width=5, height=2)
boton_7.place(x=20, y=80)

boton_8 = tk.Button(ventana, text="8", width=5, height=2)
boton_8.place(x=90, y=80)

boton_9 = tk.Button(ventana, text="9", width=5, height=2)
boton_9.place(x=160, y=80)

boton_0 = tk.Button(ventana, text="0", width=5, height=2)
boton_0.place(x=20, y=290)

boton_suma = tk.Button(ventana, text="+", width=5, height=2)
boton_suma.place(x=230, y=290)

boton_resta = tk.Button(ventana, text="-", width=5, height=2)
boton_resta.place(x=230, y=220)

boton_multiplicacion = tk.Button(ventana, text="*", width=5, height=2)
boton_multiplicacion.place(x=230, y=150)

boton_division = tk.Button(ventana, text="/", width=5, height=2)
boton_division.place(x=230, y=80)

boton_igual = tk.Button(ventana, text="=", width=5, height=2)
boton_igual.place(x=90, y=290)

ventana.mainloop()
