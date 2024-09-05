estudiantes = int(input("Ingresa el número de estudiantes: ")) # Ingresar el número de estudiantes
NumeroNotas = int(input("Ingresa el número de notas por estudiante: ")) # Ingresar el número de notas por estudiante
matricesNotas = [] # Crear una lista para almacenar las matrices de notas de cada estudiante
sumatoriasNotas = [] # Crear una lista para almacenar la sumatoria de notas por estudiante
promediosNotas = [] # Crear una lista para almacenar los promedios de notas por estudiante
print("--------------------------------------------------------------")

# Rellenar las matrices con las notas usando bucles for
for i in range(estudiantes): # Se crea un bucle con un rango de los números de estudiantes
    print(f"Estudiante {i + 1}:") # Se imprime "estudiante" y el número de estudiante
    notas = [] # Se crea una lista para almacenar las notas de cada estudiante
    for j in range(NumeroNotas): # Este for es para almacenar las notas y tiene un rango según el número de notas
        nota = int(input(f" Ingresa la nota {j + 1}: ")) # Es para pedir las notas enumeradas
        notas.append(nota) # Es para que según se vayan agregando, se guarden en la lista
    sumaNotas = sum(notas) # Calcular la sumatoria de las notas del estudiante
    promedioNotas = sumaNotas / NumeroNotas # Calcular el promedio de notas del estudiante
    sumatoriasNotas.append(sumaNotas) # Guardar la sumatoria de las notas del estudiante
    promediosNotas.append(promedioNotas) # Guardar el promedio de las notas del estudiante
    matricesNotas.append(notas) # Guardar la lista de notas del estudiante
    promedioGeneral = sum(promediosNotas)/estudiantes
    
# Imprimir las matrices de notas, sumatorias y promedios
print("--------------------------------------------------")
print("Matrices de notas de los estudiantes:") # Mensaje general que indica que se mostrarán las matrices 
for i in range(estudiantes): # Se añade un bucle para imprimir la matriz de cada estudiante con un límite que es estudiantes
    print("------------------------------------------------------------")
    print(f"Estudiante {i + 1}:") # Se indica el número del estudiante
    print(matricesNotas[i]) # Se imprime la matriz del estudiante
    print(f"Sumatoria de notas del estudiante: {sumatoriasNotas[i]}") # Se imprime la sumatoria de las notas del estudiante
    print(f"El promedio del estudiante es: {promediosNotas[i]}") # Se imprime el promedio de las notas del estudiante
    print("------------------------------------------------------------")
print("La nota general del curso es: ", promedioGeneral)
print("-------------------------------------------------------------")