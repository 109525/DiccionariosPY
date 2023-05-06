#ejercicio
#crear 1 diccionario llamado tienda, el ususario debe ingresar la cantidad de articulos que desea almacenar en la tienda, elementos (clave), precios(vaor). Si el  elemento  ya se encuentra en la tiena debe informarlo al usuario, de lo contrario debe ingresarlo. Mostrar la informacion almacenada en tienda (elemento y precio).

Tienda = {}
cantidadElementos = int(input("Ingrese la cantidad de elementos de la tienda: "))
for i in range(cantidadElementos):
    Articulo = input("Ingrese el nombre del articulo: ")
    if Articulo in Tienda:
        print(f"el articulo {Articulo} ya se encuentra en la tienda")
    else:
        Precio = int(input("ingrese el precio del {Articulo} "))
        Tienda[Articulo] = Precio
print("******************TIENDA************************")
for Articulo, Precio in Tienda.items():
    print("%s tiene un precio de: %d" %(Articulo, Precio))