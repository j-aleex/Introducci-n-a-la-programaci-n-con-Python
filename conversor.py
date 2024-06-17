
print("Bienvenido al conversor de millas a kilometros")
print("Escribe un numero en millas: ")
millas = input() #string
print("Tipo de datos de millas: ", type(millas))
#Convertir de string a numero
millas=float(millas)
#1milla = 1.609 km
kilometros=millas*1.609
print("Tipo de datos de millas: ", type(millas))
print("Millas ingresadas: ", millas)
print("Kilometros: ", kilometros)