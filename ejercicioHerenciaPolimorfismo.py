class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def presentarse(self):
        return "Hola, soy " + self.nombre + ". Mi contacto: " + self.correo

class Empleado(Persona):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo)
        self.salario = salario

    def calcular_bono(self, proyecto=None):
        return 0.0

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguajePrincipal):
        super().__init__(nombre, correo, salario)
        self.lenguajePrincipal = lenguajePrincipal

    def calcular_bono(self, proyecto=None):
        bono = self.salario * 0.10
        if proyecto and len(proyecto.tareas) > 5:
            bono += self.salario * 0.01
        return bono

    def presentarse(self):
        return "Soy " + self.nombre + ", desarrollador en " + self.lenguajePrincipal

class Analista(Empleado):
    def __init__(self, nombre, correo, salario, seniority):
        super().__init__(nombre, correo, salario)
        self.seniority = seniority

    def calcular_bono(self, proyecto=None):
        bono = self.salario * 0.08
        if self.seniority.lower() == "senior":
            bono += self.salario * 0.03
        return bono

    def presentarse(self):
        return "Soy " + self.nombre + ", analista " + self.seniority

class Gerente(Empleado):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo, salario)
        self.empleadosACargo = []

    def agregar_empleado(self, e):
        if e == self:
            print("Un gerente no puede agregarse a sí mismo.")
            return
        if e in self.empleadosACargo:
            print("Este empleado ya está en el equipo del gerente.")
            return
        self.empleadosACargo.append(e)

    def remover_empleado(self, e):
        if e in self.empleadosACargo:
            self.empleadosACargo.remove(e)

    def listar_equipo(self):
        return [empleado.nombre for empleado in self.empleadosACargo]

    def calcular_bono(self, proyecto=None):
        return self.salario * 0.15

    def presentarse(self):
        return "Soy " + self.nombre + ", gerente de un equipo de " + str(len(self.empleadosACargo)) + " personas"

class Tarea:
    contadorID = 1
    def __init__(self, descripcion, horasEstimadas):
        if horasEstimadas < 0:
            print("Las horas estimadas no pueden ser negativas.")
            horasEstimadas = 0
        self.id = Tarea.contadorID
        Tarea.contadorID += 1
        self.descripcion = descripcion
        self.horasEstimadas = horasEstimadas
        self.asignacion = None

class Proyecto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.tareas = []

    def agregar_tarea(self, descripcion, horasEstimadas):
        tarea = Tarea(descripcion, horasEstimadas)
        self.tareas.append(tarea)
        return tarea

    def asignar_empleado(self, idTarea, empleado):
        for tarea in self.tareas:
            if tarea.id == idTarea:
                tarea.asignacion = empleado
                return
        print("Tarea no encontrada.")

class Empresa:
    def __init__(self):
        self.empleados = []
        self.proyectos = []

    def agregar_empleado(self, e):
        self.empleados.append(e)

    def crear_proyecto(self, nombre, presupuesto):
        proyecto = Proyecto(nombre, presupuesto)
        self.proyectos.append(proyecto)
        return proyecto

    def asignar_empleado_a_proyecto(self, proyecto, idTarea, empleado):
        proyecto.asignar_empleado(idTarea, empleado)

empresa = Empresa()

dev = Desarrollador("Ana", "ana@gmail.com", 3000, "Python")
analista = Analista("Luis", "luis@gmail.com", 2500, "senior")
gerente = Gerente("María", "maria@gmail.com", 5000)

empresa.agregar_empleado(dev)
empresa.agregar_empleado(analista)
empresa.agregar_empleado(gerente)

gerente.agregar_empleado(dev)
gerente.agregar_empleado(analista)
gerente.agregar_empleado(gerente) 
gerente.agregar_empleado(dev)  

print("Equipo del gerente:", gerente.listar_equipo())

proyecto1 = empresa.crear_proyecto("Sistema Web", 20000)

t1 = proyecto1.agregar_tarea("Diseñar base de datos", 20)
t2 = proyecto1.agregar_tarea("Implementar API", 30)
t3 = proyecto1.agregar_tarea("Frontend", 25)

empresa.asignar_empleado_a_proyecto(proyecto1, t1.id, analista)
empresa.asignar_empleado_a_proyecto(proyecto1, t2.id, dev)

print(dev.presentarse(), "- Bono:", dev.calcular_bono(proyecto1))
print(analista.presentarse(), "- Bono:", analista.calcular_bono(proyecto1))
print(gerente.presentarse(), "- Bono:", gerente.calcular_bono(proyecto1))