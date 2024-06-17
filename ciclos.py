#Ciclos, iteracion, bucle
#while
"""
i=0

while i<10:
    if i<5:
        print("El numero", i, "es menora a 5")
    else:
        print("El numero",i, "es mayor a igual a 5")
    i+=1

print ("Termino la iteracion ")
"""

# for x in range(1, 11):
#     print(x)
while True:
    print("Escribe la obcion deseada")
    print("1: Saludar")
    print("2: Salir")

    respuesta=int(input())

    if respuesta == 1:
        print("Saludos terricolas")
    elif respuesta==2:
        break
print("Terminado programa")
