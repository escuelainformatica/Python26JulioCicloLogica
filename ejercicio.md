Ejercicio:
	Necesitamos agregar una lista de compras mediante línea de comando.
Para ello, cree lo siguiente:

1) Clase llamada "Compra" con los campos "nombre" y "precio"

```python
class Ejemplo:
    campo:tipo
    campo:tipo
```

2) Cree un ciclo que pueda ingresar la compra, para ello ingrese el nombre y precio por separado. Ejemplo:

```python
listado=[] # lista vacia

while True:
    campo1=input("ingrese el campo1 ")
    if campo1=="":
        break; # break sirve para salir    
    campo2=input("ingrese el campo2 ")
    objeto=Ejemplo() # ejemplo es la clase
    objeto.campo1=campo1
    objeto.campo2=campo2
    listado.append(objeto)

```

