#Diccionarios

agenda = {"Ana": "300",
          "Juan": "200",
          "Jose": "500"}

print("Telefono: ", agenda["Ana"])

if "Juan" in agenda:
    print("Si")
else:
    print("No")

lista2 = [i*i for i in range(1,11) if i % 2 == 0]
print(lista2)