#Lista de elementos llave:valor
#Arreglos asociativos

persona = {"nombre":"Rodrigo", 
           "edad":800,
           "apellido":"Montemayor"}

persona["apellido"]="Lozano"
persona["apodo"]="Rinda Tech"

print(persona["apellido"])

print(persona)

#print(persona.items())

print("direccion" in persona)

"""for key, value in persona.items():
    print(f"La llave {key} tiene el valor {value}")"""
