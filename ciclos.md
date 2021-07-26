# while

Lo voy a usar cuando no se cuando termina la operación. Por ejemplo, si leo un archivo de texto , línea a línea , no se cuantas línea tiene (hasta que llegue al final)

```python
while <condicion>: # hasta que la condicion deje de cumplirse
    <codigo que quiero que se repita>

numero1=0    
while numero1<10:
	numero1=numero1+1       
```

# for

Cuando tengo un "listado" de valores (list, diccionario, tuple, etc.)

```python
for fila in filas:
	<codigo que quiero repetir>
    
paises=["Chile","Argentina","Peru"]    
for pais in paises:
    print(pais)
        
```

"For" de la manera clásica

```python
for i in range(0,100,1): # muestra del 0 hasta el 99 saltando de 1 en 1.
	print(i)
```

# Salir del ciclo

Una forma de salir, es escribiendo "break"

```python
while True: # ciclo infinito
	# codigo
	if valor==1:
		 break # sale del ciclo while inmediatamente
	# codigo
```

## funcionalidades del ciclo

* mostrar
* filtrar
* buscar
* operar (sumatoria)



```python
paises=["Chile","Argentina","Peru","Chile"]    

# mostrar
for pais in paises:
    print(pais)
    
# filtrar  (muestra Chile dos veces)
for pais in paises:
    if(pais=="Chile"):
	    print(pais)  
        
# buscar  (muestra Chile dos veces)
for pais in paises:
    if(pais=="Chile"):
	    print(pais)  
        break

# sumatoria de numeros        
numeros=[10,20,30,40]        
total=0
for numero in numeros:
    total=total+numeros
    
    

        
```

