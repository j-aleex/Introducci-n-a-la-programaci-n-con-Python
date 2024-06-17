print("******SUPER MERCADO******")
print("******Bienvenido******")
lista=[]

productos_totales=0

def mostrar_Menu():
    print()
    print("1: Ingresar lista")
    print("2: Mostrar lista")
    print("3. Salir ")

def ingresar_lista():
    
    carrito=[]
    while True:
        print("¿Que productos deseas comprar? Solo puedes elegir 1 de cada especie")
        print("Escribe F para terminar la lista o V para ver tu carrito")
        producto=input()
        if producto=="F": break
        elif producto=="V":
            print(f"Tu lista de compras tiene: {carrito}")
            continue
        elif producto not in carrito:
            carrito.append(producto)
        else: 
            print("Ese animal ya se encuentra en el carrito")
            #print("Has comprado un: ",animal)
       
        lista.append(producto)

def mostrarLista():
   print("")
   print("Tu lista es: ")
   for compra in lista:           
      print(f"Lista{lista}") 


while True:
    mostrar_Menu()
    respuesta=int(input())

    if(respuesta==1):
      ingresar_lista()
    elif(respuesta==2):
      mostrarLista()
    elif(respuesta==3):
     break
    else:
      print("Opcion Incorrecta")
      break
