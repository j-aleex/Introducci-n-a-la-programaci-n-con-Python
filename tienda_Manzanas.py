print("****Bienvenido a la tienda de manzanas*****")
print("Ingrese su nombre: ")
nombre=input()
manzanas=int(20)
precio=float(5)
print("Bienvenido ", nombre, " \nManzanas disponibles", manzanas, "\nPrecio ", precio," soles")
print("Cuantas manzanas quiere comprar: ")
compra=input()
compra=int(compra)
total=precio*compra

print("Cantidad de manzanas compradas: ", compra,"Total: ",total)
cantidad=manzanas-compra
print("Cantidad Disponible", cantidad)

