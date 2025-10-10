import pytest
from modelos import Producto, LineaFactura, Cliente
from excepciones import ProductosError, ClientesError, DescuentosError


def test_producto_crear():
    p = Producto(1, "Manzana", "alimentos", 2500)
    assert p.codigo == 1
    assert p.nombre == "Manzana"
    assert p.categoria == "alimentos"
    assert p.precio == 2500

@pytest.mark.parametrize("precio", [-2500, -5000.50])
def test_producto_precio(precio):
    with pytest.raises(ProductosError) as exc:
        Producto(1, "Manzana", "Alimentos", precio)
    assert "no puede ser negativo" in str (exc.value).lower()

@pytest.mark.parametrize("precio", ["cinco mil", object(), None])
def test_precio_producto_nonumero(precio):
    with pytest.raises(ProductosError) as exc:
        Producto(1, "Manzana", "Alimentos", precio)
    assert "Error en el precio del producto" in str(exc.value)

def test_categoria_noPermitida():
    with pytest.raises(ProductosError) as exc:
        Producto(1, "Manzana", "Mascotas", 2500)
    assert "Categoria no permitida" in str(exc.value)

def test_producto_categoria_minuscula():
    p = Producto(1, "Manzana", "Alimentos", 2500)
    assert p.categoria == "alimentos"

def test_cliente_valido():
    c = Cliente(123, "Juan", True)
    assert c.id == 123
    assert c.nombre == "Juan"
    assert c.vip == True

@pytest.mark.parametrize("valor", ["uno", None, object()])
def test_cliente_id(valor):
    with pytest.raises(ClientesError) as exc:
        Cliente(valor , "Juan", False)
    assert "Error en la identificacion del cliente."

def test_linea_factura_subtotal():
    p = Producto(10, "Pan", "alimentos", 1500)
    linea = LineaFactura(p, 5)
    assert linea.subtotal == 7500