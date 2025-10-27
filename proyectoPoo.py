import random
from typing import List, ClassVar, Set
from abc import ABC, abstractmethod
from dataclases import dataclass

class Productos:
    def __init__(self, nombre, precio, talla, color):
        self.nombre = nombre 
        self.precio = precio
        self.talla = talla
        self.color = color

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaProductos = [Productos]

    def agregar_productos(self, producto = Productos):
        self.listaProductos.append(producto)
        print(f'El producto ha sido agregado exitosamente')

    def mostrar_productos(self):
        contador = 0
        for i in self.listaProductos:
            contador += 1
            print(f'Producto {contador}: {i.nombre}: {i.precio}$, Talla: {i.talla}, Color: {i.color}')

    def crear_producto(self, nNombre, nPrecio, nTalla, nColor):
        categoria = input("Ingrese la categoria que desea añadir (Ropa/Tenis): ").lower()
        nNombre = input("Ingrese el nombre: ")
        nPrecio = int(input("Ingrese el precio"))
        nTalla = input("Ingrese la talla (S/M/L): ")
        nColor = input("Ingrese el color: ")
        if categoria == "ropa":
            nProducto = Ropa(nNombre, nPrecio, nTalla, nColor)
            print(f'El producto ha sido creado exitosamente. ({nProducto.nombre})')
            
        if categoria == "tenis":
            nProducto = Tenis(nNombre, nPrecio, nTalla, nColor)
            print(f'El producto ha sido creado exitosamente. ({nProducto.nombre})')


class Ropa(Productos):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre, precio, talla, color)

class Tenis(Productos):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre, precio, talla, color)

class cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = Carrito()

class Carrito: 
    def __init__(self):
        self.listaproductos = []
    
    def mostrar_carrito(self):
        contador = 0
        for i in self.listaproductos:
            contador += 1
            print(f'Producto {contador}: {i.nombre}: {i.precio}$, Talla: {i.talla}, Color: {i.color}')

    def calcular_total(self):
        acumulador = 0
        for i in self.listaproductos:
            acumulador = acumulador + i.precio
        return acumulador

class Pedido():
    def __init__(self, cliente):
        self.idPedido = (random.randint(1000,9999))
        self.cliente = cliente

    def mostrar_factura(self):
        print(f'{self.cliente.nombre}, su pedido tiene id {self.idPedido}. Fue enviado al correo {self.cliente.correo}')

        

producto0 = Productos("Prueba")

camisa = Ropa("camisa", 3000, "M", "Rojo")
buzo = Ropa("buzo", 5000, "M", "Negro")
chaqueta = Ropa("chaqueta", 7000, "M", "Blanco")

botas = Tenis("botas", 6000, "38", "Azul")
tenis = Tenis("tenis", 6000, "38", "Naranja")
chanclas = Tenis("chanclas", 6000, "38", "Azul")


print("Ingrese su nombre y correo para crearle su carrito:")
nombreNuevo = input("Nombre: ")
correoNuevo = input("Correo: ")
clienteNuevo = cliente(nombreNuevo, correoNuevo)


        
