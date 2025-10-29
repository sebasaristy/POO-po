import pytest
from tallerMico.proyecto.proyectoPoo import Productos, Ropa, Tenis, Tienda, Cliente, Carrito, Pedido

def test_creacion_ropa():
    p = Ropa("Camisa", 5000, "M", "Rojo")
    assert p.nombre == "Camisa"
    assert p.precio == 5000
    assert p.talla == "M"
    assert p.color == "Rojo"

def test_creacion_tenis():
    t = Tenis("Tenis", 2500, 42, "Blanco")
    assert isinstance(t, Productos)
    assert t.talla == 42

def test_mostrar_info():
    p = Ropa("Camisa", 5000, "M", "Rojo")
    texto = p.mostrar_info()
    assert "Camisa" in texto
    assert "Rojo" in texto
    
def test_agregar_mostrar_productos():
    tienda = Tienda("Moda")
    p1 = Ropa("Camisa", 3000, "S", "Azul")
    p2 = Tenis("Adidas", 2000, 41, "Negro")
    tienda.agregar_productos(p1)
    tienda.agregar_productos(p2)
    tienda.mostrar_productos()
    assert len(tienda.listaProductos) == 2
    assert tienda.listaProductos[0].nombre == "Camisa"
    assert tienda.listaProductos[1].nombre == "Adidas"
    
def test_carrito_agregar():
    carrito = Carrito()
    p1 = Ropa("Camisa", 5000, "S", "Rojo")
    p2 = Tenis("Puma", 10000, 41, "Gris")
    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)
    assert len(carrito.listaproductos) == 2
    assert carrito.calcular_total() == 15000

def test_carrito_eliminar():
    carrito = Carrito()
    p1 = Ropa("Camisa", 5000, "S", "Rojo")
    p2 = Tenis("Puma", 10000, 41, "Gris")
    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)

    carrito.eliminar_producto("Camisa")
    assert len(carrito.listaproductos) == 1
    assert carrito.listaproductos[0].nombre == "Puma"

def test_cliente_carrito():
    cliente = Cliente("mico", "correo@mi.com")
    assert cliente.nombre == "mico"
    assert cliente.correo == "correo@mi.com"
    assert isinstance(cliente.carrito, Carrito)
    cliente.mostrar_cliente()

def test_pedido_con_total():
    cliente = Cliente("mico", "correo@mi.com")
    p1 = Ropa("Camisa", 5000, "S", "Rojo")
    p2 = Tenis("Puma", 10000, 41, "Gris")
    cliente.carrito.agregar_producto(p1)
    cliente.carrito.agregar_producto(p2)
    pedido = Pedido(cliente)
    assert pedido.cliente.nombre == "mico"
    assert pedido.total == 15000
    assert isinstance(pedido.idPedido, int)

def test_tienda_sin_productos():
    tienda = Tienda("Vacia")
    assert tienda.listaProductos == []
    tienda.mostrar_productos()

def test_carrito_vacio():
    carrito = Carrito()
    assert carrito.calcular_total() == 0

def test_eliminar_producto_inexistente():
    carrito = Carrito()
    p1 = Ropa("Camisa", 5000, "S", "Rojo")
    carrito.agregar_producto(p1)
    carrito.eliminar_producto("Pantalon")
    assert len(carrito.listaproductos) == 1
    assert carrito.listaproductos[0].nombre == "Camisa"

def test_mostrar_factura():
    cliente = Cliente("Mico", "miquito")
    p1 = Ropa("Camisa", 5000, "S", "Rojo")
    p2 = Tenis("Puma", 10000, 41, "Gris")
    cliente.carrito.agregar_producto(p1)
    cliente.carrito.agregar_producto(p2)
    pedido = Pedido(cliente)
    factura = pedido.mostrar_factura()
    assert isinstance(factura, str) or factura is None
    assert hasattr(pedido, "idPedido")

def test_agregar_varios_productos():
    tienda = Tienda("MicoStore")
    productos = [
        Ropa("Buzo", 6000, "L", "Negro"),
        Tenis("Nike", 3000, 42, "Rojo"),
        Ropa("Pantalon", 8000, "M", "Beige"),
    ]
    for p in productos: 
        tienda.agregar_productos(p)

    assert len(tienda.listaProductos) == 3
    assert any(isinstance(p, Ropa) for p in tienda.listaProductos)
    assert any(isinstance(p, Tenis) for p in tienda.listaProductos)

def test_pedido_carrito_vacio():
    cliente = Cliente("Mico", "mico@")
    pedido = Pedido(cliente)
    assert pedido.total == 0

def test_tipo_datos():
   p1 = Ropa("Camisa", 5000, "S", "Rojo")
   assert isinstance(p1.nombre, str)
   assert isinstance(p1.precio, int)
   assert isinstance(p1.talla, str)
   assert isinstance(p1.color, str)

