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

nombreEstudiante = input("Ingrese nombre estudiante: ")
edadEstudiante = int(input("Ingrese la edad del estudiante: "))
notaUnoEstudiante = float(input("Ingrese la nota 1: "))
notaDosEstudiante = float(input("Ingrese la nota 2: "))
notaTresEstudiante = float(input("Ingrese la nota 3: "))

estudiante = controlAcademico(nombreEstudiante, edadEstudiante, notaUnoEstudiante, notaDosEstudiante, notaTresEstudiante)
promedioEstudiante = estudiante.promedio()

print("El promedio de ", estudiante.nombre, "es de: ", promedioEstudiante)