import random

def tirar_dados():
    return random.randint(2,12)

def pedir_respuesta():
    print("Ingresa tu predición: ")
    print("1. Par")
    print("1. Impar")
    print("3. Salir del juego")

    return int(input())

def imprimir_resultado(numero, resultado):
    # not , %
    # Sabes si un numero es par o impar
    #Dividirlo entre 2 y si el remanente es 0, es par ,. Si es 1, es impar
    #Resultado=5/2= REsultado seria 2 con remanente 1 
    #Resultado=6/2 Resultado seria 3, con remanten 0

    es_par=numero % 2 ==0

    if es_par and prediccion ==1:
        print("Ganaste!, numero de los dados: ", numero)
    elif not es_par and prediccion==2:
        print("Ganaste, numero de los dados: ", numero)
    else: 
        print("Perdiste, umero de los dados: ", numero)


while True:
    numero=tirar_dados()
    prediccion= pedir_respuesta()
    if prediccion==3:
        break 
    imprimir_resultado(numero, prediccion)

print("Gracias por jugar")
#print("Tiro de dados: ", tirar_dados())