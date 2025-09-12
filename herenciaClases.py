class persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print(f'{self.nombre} está respirando')

class estudiante(persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def estudiar(self):
        print(f'{self.nombre} está estudiando {self.carrera}')

persona1 = persona("Juan")
persona1.respirar()

persona2 = estudiante("Camila", "Comunicacion")
persona2.estudiar()