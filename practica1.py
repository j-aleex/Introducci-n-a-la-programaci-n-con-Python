print("Ingrese un número entre el 1 y 100: ")

while True:
    numero = int(input())
    if(numero < 1):
        print(f"Favor de ingresar un numero mayor a 0, usted ingreso {numero}")
    elif(numero > 100):
        print(f"Favor de ingresar un numero menor o igual a 100, usted ingreso {numero}")
    else:
        print(f"Muy bien! El {numero} es una gran opcion")
        break