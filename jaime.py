class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f'El perro que está ladrando es: ', self.nombre)
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

print("Chirri")

miPerro = Perro("Fernanfloo", "Mico")
segundoPerro = Perro("Cesar", "Velasquez")
miPersona = Persona("Sebastian", 18, "Nunca")

print("Ingrese los datos de su perro")
nombrePerro3 = input("Ingrese el nombre del perro: ")
razaPerro3= input("Ingrese la raza del perro: ")
perro3 = Perro(nombrePerro3, razaPerro3)

miPerro.ladrar()