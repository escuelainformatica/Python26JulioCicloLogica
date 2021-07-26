# clase de servicio, es una coleccion de funciones.
# se refiere a verbos o acciones.
# es una clase de servicio
# que es una clase de servicio? Es una coleccion de funciones.
from modelos.Producto import Producto


class ProductoServicio:
    def mostrar(self, productos: list):
        # for i=0;i<10;i++
        # en python solo se pueden escribir ciclos for (for-each)
        for producto in productos:
            print(producto.nombre, producto.stock)

    def agregar(self, productos: list, producto_nuevo: Producto) -> None:
        productos.append(producto_nuevo)

    def vender(self, productos: list, nombre, cantidad):
        for producto in productos:
            if producto.nombre == nombre:
                producto.stock = producto.stock - cantidad
            else:
                print("no es el producto buscando " + producto.nombre)

    def funcionejemplo(self):
        pass
