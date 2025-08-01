class controlAcademico:
    def __init__(self, nombre, edad, notaUno, notaDos, notaTres):
        self.nombre = nombre
        self.edad = edad
        self.notaUno = notaUno
        self.notaDos = notaDos
        self.notaTres = notaTres

    def promedio(self):
        promedio = (self.notaUno + self.notaDos + self.notaTres)/3
        return promedio
    
    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota 1: ", self.notaUno)
        print("Nota 2: ", self.notaDos)
        print("Nota 3: ", self.notaTres)

    promedioEstudiante = promedio

print("Sistema de gestion de estudiantes")
listaEstudiantes = []
while True: 
    print("\nSeleccione la opcion que desea:")
    print("1. Agregar estudiante")
    print("2. Mostrar informacion de estudiantes")
    print("0. Salir")
    opcion = int(input("Ingrese el numero: "))

    if opcion == 1:
        nombreEstudiante = input("Ingrese nombre estudiante: ")
        edadEstudiante = int(input("Ingrese la edad del estudiante: "))
        notaUnoEstudiante = float(input("Ingrese la nota 1: "))
        notaDosEstudiante = float(input("Ingrese la nota 2: "))
        notaTresEstudiante = float(input("Ingrese la nota 3: "))
        estudianteNuevo = controlAcademico(nombreEstudiante, edadEstudiante, notaUnoEstudiante, notaDosEstudiante, notaTresEstudiante)    
        listaEstudiantes.append(estudianteNuevo)
    
    if opcion == 2:
        numeroEstudiantes = len(listaEstudiantes)
        print(f'\nEl numero de Estudiantes es de {numeroEstudiantes}')
        for estudiante in listaEstudiantes:
            print("El nombre del Estudiante es: ", estudiante.nombre)
            print("El promedio del estudiante es: ", estudiante.promedio())

    if opcion == 0:
        print("Gracias")
        break