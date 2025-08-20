import random 
listaNumero2 = [i for i in range(0,10)]
listaNumero = [] 
longitudListanumeros = len(listaNumero)
for i in range(0,10):
    listaNumero.append(random.randint(1,100))

listaNumero.sort()
print(listaNumero)

for i in (listaNumero):
    if i == 1:
        print("care mico")

class persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numeros = [random.randint(100,999) for i in range (0,5)]

    def generarNumeros(self):
        self.numeros = [random.randint(100,999) for i in range (0,5)]

while True:
    print("\nBienvenido a la rifa")
    nombrePersona = input("Ingrese su nombre: ")
    nuevaPersona = persona(nombrePersona)

    print(f'\n{nuevaPersona.nombre}, sus numeros son {nuevaPersona.numeros}')

    
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