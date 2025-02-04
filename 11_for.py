"""
for 
"""

nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]
edades = [25, 30, 35, 40, 45]

# para cada nombre en nombres ...
for nombre in nombres:
    print(nombre)

print(nombre)

# Ejercicio 1
import os
os.system("cls")


# Mostrar los nombres que empiezan por "P"
check = "P"
# Crear el bucle para acceder a cada elemento de la lista
for nombre in nombres:
    # if nombre[0].lower() == check.lower():
    #     print(nombre.capitalize())
    if nombre.lower().startswith(check.lower()):
        print(nombre.capitalize())

# Ejercicio 2
# Mostrar los numeros de esta lista que empiezan por 2
edades = [25, 30, 35, 40, 45, 28, 24, 76, 89, 234]

check = 2
suma = 0
for edad in edades:
    if str(edad).startswith(str(check)):
        print(edad, end=" ")
        suma += edad
print(end = "\n")

print(suma)

# Ejercicio 3
# Mostrar el resultado así :
"""
la suma de los elementos es X
hay X elementos
el promedio de la lista es X

"""

# Ejercicio
# Mostrar si un nombre está en lista
nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]

nombre_a_buscar = "Luis" # "Alba"
# "Luis está en la lista"
# "Alba no está en la lista" 

for nombre in nombres:
    print(nombre)
    if nombre.lower() == nombre_a_buscar.lower():
        print(f"{nombre_a_buscar} está en la lista")
        break
else:
    print(f"{nombre_a_buscar} no está en la lista")

# Quiero saber qué nombres de la lista contiene la letra "o"
nombres_con_o = []

for nombre in nombres:
    indice = nombres.index(nombre)
    if "o" in nombre.lower():
        print(f"{indice + 1}. {nombre}")
        nombres_con_o.append(nombre)

# print(nombres_con_o)

print(list(range(10)))

for num in range(10):
    print(num)

# for(let i= 0; i< nombres.lenght; i++)
for index in range(len(nombres)):
    print(f"{index} {nombres[index]}")

