# clase de modelo, es una definicion de datos (grupo de variables)
class Producto:
    precio: int
    nombre: str
    stock: int

    """constructor"""

    def __init__(self, precio=0, nombre="", stock=0):
        self.precio = precio
        self.nombre = nombre
        self.stock = stock
