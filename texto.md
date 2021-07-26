
# por defecto los argumentos se pasan por valor
def funcion1(argumento):
    argumento = 20


# aqui se pasa la variable por referencia (puntero)
def funcion2(arg):
    arg = ["a", "b", "c"]  # ya no usa la memoria que tiene listado, usa una memoria diferente.
    # arg.append("nuevo")


variable1 = 0
funcion1(variable1)
listado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
funcion2(listado)

cocacola = Producto(222, "cocacola", 10)
fanta = Producto(555, "fanta", 30)

productos = [cocacola, fanta]  # lista de productos ()=tuples, { } = set/diccionario []=lista

print(productos)

sprite = Producto(777, "sprite", 60)

agregar_producto(productos, sprite)

print(productos)


# ciclos
# for (for-each), while

# logica
# if, else, elif
print("---------- frutas --------------")
frutas=["peras","manzanas","uvas","naranjas","peras","duraznos","sandia"] # lista de productos ()=tuples, { } = set/diccionario []=lista
i=0

print("while---")
i=0
while i< len(frutas):
    print(frutas[i],i)
    i=i+1

finalizar=False

while finalizar==False:
    fruta=input("ingrese una fruta o vacio para salir:")
    if fruta!="":
        frutas.append(fruta)
    else:
        finalizar=True

for fruta in frutas:
    print(fruta,i)
    i=i+1

numero1=1
numero2=2
numero3=3
#  && and
#  || and
if numero1==numero2 and numero2==numero3:
    print("todas las variables son iguales")
elif numero1==numero2 and numero2!=numero3:
    print("solo numero1 y numero2 son iguales")
elif numero1!=numero2 and numero2==numero3:
    print("solo numero2 y numero3 son iguales")
elif numero1==numero3 and numero1!=numero2:
    print("solo numero1 y numero3 son iguales")
else:
    print("no son iguales")

if not numero1!=numero2 and not numero2!=numero3:
    print("todas las variables son iguales")

numero1=2
numero2=2

if numero1>numero2:
    print("numero 1 es mayor")
elif numero1<numero2:
    print("numero 2 es mayor")
else:
    print("son iguales")


if numero1>numero2:
    print("numero 1 es mayor")
else:
    if numero1<numero2:
        print("numero 2 es mayor")
    else:
        print("son iguales")











