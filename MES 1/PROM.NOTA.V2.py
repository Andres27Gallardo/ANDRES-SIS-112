print("-------------------------------------------------------------")
estudiantes = int(input("Ingresa el número de estudiantes: "))# Ingresar el número de estudiantes
NumeroNotas = int(input("Ingresa el número de notas por estudiante: "))# Ingresar el número de notas por estudiante
matricesNotas = []# Crear una lista para almacenar las matrices de notas de cada estudiante
print("--------------------------------------------------------------")

# Rellenar las matrices con las notas usando bucles for
for i in range(estudiantes):#Se crea un bucle con un rango de los numeros de estudiantes
    print(f"Estudiante {i + 1}:")#Se imprime "estudiante" y el numero de estudiante
    notas = []#Se crea una matriz para almacenar las notas de cada estudiantes
    for j in range(NumeroNotas):#Este for es para almacenar las notas y tiene un rango segun el numero de notas
        nota = int(input(f" Ingresa la nota {j + 1}: "))#Es para pedir las notas ennumeradas
        notas.append(nota)#Es para que segun se vaya agregando, vaya llendo al ultimo
    matricesNotas.append(notas)#Es para que segun el numero de estudiantes se vayan al ultimo

# Imprimir las matrices de notas
print("--------------------------------------------------")
print("Matrices de notas de los estudiantes:")#Mensaje general que indica que se mostrara las matrices 
for i in range(estudiantes):#Se añade un buble para imprimir las matrice de cada estudiante con un limete que es estudiantes
    print(f"Estudiante {i + 1}:")#Se inica el numero del estudiante
    print(matricesNotas[i])#Se imprime la matriz del estudiantes

