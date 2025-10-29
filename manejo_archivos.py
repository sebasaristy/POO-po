
class Estudiantes:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio 

    def aprobo(self):
        return self.promedio >= 3.0 
    
class Curso:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f'Estudiante agregado exitosamente: {estudiante.nombre}')
        with open(self.nombre_archivo, "a") as f:
            f.write(f'{estudiante.nombre}, {estudiante.promedio}\n')

    def guardar_en_archivo(self):
        try:
            with open(self.nombre_archivo, "w") as f:
                for e in self.estudiantes:
                    f.write(f'{e.nombre}, {e.promedio}\n') 
            print("Estudiantes guardados exitosamente")

        except:
            print("Hubo un error al guardar los estudiantes")
    
    def mostrar_estudiantes(self):
        for e in self.estudiantes:
            print(f'{e.nombre} tiene un promedio de {e.promedio}')

    def cargar_desde_archivo(self):
        self.estudiantes = []
        try: 
            with open(self.nombre_archivo, "r") as f:
                for linea in f:
                    nombre , promedio = linea.strip().split(",")
                    estudiante = Estudiantes(nombre, promedio)
                    self.estudiantes.append(estudiante)
        except:
            print("Hubo un error cargando los estudiantes")


poo = Curso("estudiantes.txt")
estudiante1 = Estudiantes("Mico", 3.3)
estudiante2 = Estudiantes("Mario", 4.1)
estudiante3 = Estudiantes("Juana", 2.5)
poo.agregar_estudiante(estudiante3)
poo.cargar_desde_archivo()
poo.mostrar_estudiantes()

def cargar_medios_de_transporte(self):
        with open("transportes.txt", "r") as f:
            for linea in f:
                linea = linea.strip().split(",")
                if linea[0] == "Bicicleta":
                    self.transportes.append(Bicicleta(int(linea[1]), int(linea[2]), float(linea[3])))
                elif linea[0] == "Moto":
                    self.transportes.append(Moto(int(linea[1]), int(linea[2]), float(linea[3])))
                elif linea[0] == "Furgoneta":
                    self.transportes.append(Furgoneta(int(linea[1]), int(linea[2]), float(linea[3])))
    