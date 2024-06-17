nombres = ["Rodrigo", "Juan","Santiago", "Pedro", "jorge", " ray "]
print(nombres)

for n in nombres:
    print("Se inscribio en la lista ", n)

#Enumerar lista
for i, n in enumerate(nombres):
    print("Se inscribio en la lista ",i, n)
#f-strings
    print(f"Se inscribio {n} en la lista con el indice{i}")

# #0= rodrigo, 1=juan, 2=pedro
# print(len(nombres))
# #agregar append
# nombres.append("Jorge")
# print(nombres)
# #Borrar nombres remove
# nombres.remove("Rodrigo")
# print(nombres)

# #busqueda en lista
# print("Rodrigo" in nombres)

# #busqueda espesifica:  muestrame desde inicio a 3 u de 3 a 5
# print("Bienvenido: ",nombres[:3])
# print("Lo sentimos: ", nombres[3:5])
# #Busqueda desde un numero especifico hasta el final
# print("Lo sentimos: ", nombres[3:])


