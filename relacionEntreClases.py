#Vas a crear un pequeño sistema de calificaciones con las clases Estudiante y Curso. 
#Cada una deberá definirse con su propio constructor y métodos que operen sobre los atributos de instancia.

class Estudiantes:
    def __init__(self, nombre: str, edad: int, calificaciones: list[float]):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
        self.promedio = 0

    def calcular_promedio(self):
        j = 0
        for i in range (0,len(self.calificaciones)):
            j = j + (self.calificaciones[i])
        promedio = j/len(self.calificaciones)
        self.promedio = promedio
    
    def mostrar_info(self):
        print(f'Estudiante: {self.nombre}(Edad: {self.edad}) -- Promedio: {self.promedio: .2f}')
    

class curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def promedio_general(self):
        suma = 0
        for k in range(0, len(self.estudiantes)):
            suma = suma + curso1.estudiantes[k].promedio
            promGen = suma/len(self.estudiantes)
        print(f'Promedio general: {promGen: .2f}')
    
    def mostrar_estudiantes(self):
        for j in range (0, len(self.estudiantes)):
            Estudiantes.mostrar_info(self.estudiantes[j])

s1 = Estudiantes("Ana", 20, [4.5, 3.7, 5.0])
s2 = Estudiantes("Luis", 22, [4.0, 4.2, 3,8])
s3 = Estudiantes("Maria", 19, [5.0, 5.0, 4.9])
curso1 = curso("Algebra Lineal")
curso1.agregar_estudiante(s1)
curso1.agregar_estudiante(s2)
curso1.agregar_estudiante(s3)

s1.calcular_promedio()
s2.calcular_promedio()
s3.calcular_promedio()

curso1.promedio_general()
curso1.mostrar_estudiantes()

class Estudiantes:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota


class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experiencia = experiencia

class grupoAsignatura:
    def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.horario = horario 
        self.codigo = codigo
        self.profesor = profesor 
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante agregado")
    
    def promedio(self):
        acumulador = 0
        for estudiante in self.estudiantes:
            acumulador = acumulador + estudiante.nota
        promedio = acumulador/len(self.estudiantes)
        return promedio 
    
    def mostrar_info(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)
    

profesor1 = Profesor("Cesar", 25, 2)
clase1 = grupoAsignatura("POO", "M-V 10-12", "62", profesor1)
estudiante1 = Estudiantes("Cesar", 18, 3.8)
estudiante2 = Estudiantes("Emmanuel", 18, 1.0)
estudiante3 = Estudiantes("Sebastian", 18, 3.8)

clase1.agregar_estudiante(estudiante1)
clase1.agregar_estudiante(estudiante2)
clase1.agregar_estudiante(estudiante3)

print(clase1.mostrar_info())
print(clase1.promedio())
