from datetime import datetime

print("******************************")
print("******   BIENVENIDO A *******")
print("**  LA TIENDA DE MASCOTAS **")
print("******************************")

"""num_perros=10
num_gatos=8
num_pajaros=25"""

inventario={
    "Perro": 10,
    "Gato" : 8,
    "pajaros": 25,
    "iguana": 2
}

animales_totales = 0

for val in inventario.values():
    animales_totales+=val

#animales_totales=num_perros+num_pajaros+num_gatos

print("Por favor ingresa tu nombre")
nombre=input()
print("Porfavor escribe tu apellido")
apellido=input()

#Concatenacion
nombre_completo= nombre + " " +apellido
print("Gracias por visitarno,", nombre_completo)

compras=[]

def mostrar_menu():
    print("")
    print("===============================")
    print("Selecciona la opcion q deseas: ")
    print("1: Conocer cuantos animales tiene la tienda")
    print("2: Comprar un animal")
    print("3: Mostrar compras")
    print("4: Salir")

def mostrar_inventario():
    print("*****Inventario*******")
    #print("Actualmente contamos con: ")
    for llave,valor in inventario.items():
        print(f" {llave}:{valor}")
    #print("Perros: ", num_perros, "Gatos: ", num_gatos, "Pajaros: ",num_pajaros)
    print("En total tenemos: ",animales_totales, " animales")

def comprar_animal():
    carrito=[]

    while True:
        print("¿Que animales deseas comprar? Solo puedes elegir 1 de cada especie")
        print("Escribe F para terminar la lista o V para ver tu carrito")
        animal=input()

        if animal == "F" : break

        if animal == "V":
            print(f"Tu carrito de comorar contiene {carrito}")
            continue

        if animal not in inventario:
            print(f" Lo sentimos, no contamos con el animal {animal}")
        elif inventario[animal] == 0:
            print(f"Lo sentimos, no tenemos en existencia el animal {animal}")
        elif animal not in carrito:
            carrito.append(animal)
        else: 
            print("Ese animal ya se encuentra en el carrito")
        #print("Has comprado un: ",animal)
    
    print("El contendo de tu carrio es: ")
    for animal in carrito:
        print("  ",animal)
        inventario[animal]-=1

     #Agregar esta compra al carrito de compras
    fecha=datetime.now()
    compras.append( (nombre, carrito, fecha) ) #tupla

def mostrar_compras():

    print("")
    print("Compras realizadas: ")
    for compra in compras:           
        print(f" {compra[0]} compró{compra[1]} en {compra[2]}") 

while True:
    mostrar_menu()
    respuesta= int(input())

    if respuesta==1:
        mostrar_inventario()
    elif respuesta==2:
        comprar_animal()
    elif respuesta==3:
        mostrar_compras()
    elif respuesta==4:
        break
print("Termino el programa")    

# print("Actualmente contamos con: ")
# print("Perros: ", num_perros, "Gatos: ", num_gatos, "Pajaros: ",num_pajaros)
# print("En total tenemos: ",animales_totales, " animales")