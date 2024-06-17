print("Ingresa numero: ")
num1=int(input())

print("Ingresa numero: ")
num2=int(input())

def miFuncion(operacion, num1, num2):
    if operacion == 1: 
        return num1+num2
    elif operacion == 2: 
        return num1-num2
    elif operacion == 3: 
        return num1*num2
    elif operacion == 4: 
        return num1/num2


while True:
    print(" 1. Sumar")
    print(" 2. Restar")
    print(" 3. Multiplicar")
    print(" 4. Dividir")
    print(" 5. Salir")

    numero=int (input())

    if( numero in [1,2,3,4]):
        print("El resultado es: ", miFuncion(numero, num1,num2))
    elif(numero==5):
        print("Programa terminado")
        break
   
    else:
        print("Intenta de nuevo")