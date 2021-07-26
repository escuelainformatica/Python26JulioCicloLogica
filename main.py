# ventas de productos <-- que es un producto?
# modelo o datos que vamos a trabajar.
# acciones (venta)

# tuple, seq, diccionary, clase

# clase de modelo (solo propiedades)

class Producto:
    precio: int
    nombre: str
    stock: int

    """constructor"""

    def __init__(self, precio=0, nombre="", stock=0):
        self.precio = precio
        self.nombre = nombre
        self.stock = stock


# while, for

def mostrar_productos(productos: list):
    # for i=0;i<10;i++
    # en python solo se pueden escribir ciclos for (for-each)
    for producto in productos:
        print(producto.nombre,producto.stock)


def agregar_producto(productos: list, producto_nuevo: Producto) -> None:
    productos.append(producto_nuevo)


def vender_producto(productos: list, nombre, cantidad):
    for producto in productos:
        if producto.nombre == nombre:
            producto.stock=producto.stock-cantidad
        else:
            print("no es el producto buscando "+producto.nombre)



cocacola = Producto(222, "cocacola", 10)
fanta = Producto(555, "fanta", 30)

productos = [cocacola, fanta]  # lista de productos ()=tuples, { } = set/diccionario []=lista

mostrar_productos(productos)

vender_producto(productos,"fanta",5)

mostrar_productos(productos)

