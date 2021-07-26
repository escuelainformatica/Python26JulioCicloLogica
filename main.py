# modelos/ProductoServicio.py importo solo la clase
from modelos.Producto import Producto # as P
from servicios.ProductoServicio import ProductoServicio

# ventas de productos <-- que es un producto?
# modelo o datos que vamos a trabajar.
# acciones (venta)

# tuple, seq, diccionary, clase

# clase de modelo (solo propiedades)

# clase de modelo


# while, for


ps=ProductoServicio()

cocacola = Producto(222, "cocacola", 10)
fanta = Producto(555, "fanta", 30)

productos = [cocacola, fanta]  # lista de productos ()=tuples, { } = set/diccionario []=lista

ps.mostrar(productos)

ps.vender(productos,"fanta",5)

ps.mostrar(productos)

