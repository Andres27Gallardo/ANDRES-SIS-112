estudiantes = int(input("Ingrese a cuantos estuadiantes quiere calificar: "))
total = estudiantes
suma = 0
while estudiantes > 0:
    nota = float(input("nota : "))
    suma = suma+nota
    estudiantes -= 1
promedio = suma/total
print(promedio)
