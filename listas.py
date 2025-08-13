import random 
"""listaNumero2 = [i for i in range(0,10)]
listaNumero = [] 
longitudListanumeros = len(listaNumero)
for i in range(0,10):
    listaNumero.append(random.randint(1,100))

listaNumero.sort()
print(listaNumero)

for i in (listaNumero):
    if i == 1:
        print("care mico")"""

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

    
