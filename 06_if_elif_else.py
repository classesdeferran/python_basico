"""
IF / ELIF / ELSE
Control de condiciones
"""

# Condición binaria 
llueve = True

if llueve:
    print("Cogeré el paraguas")
else:
    print("Iré a pasear")

print("Resto del código")

lunes = False # los lunes como pizza
jueves = True # jueves, paella
# el resto de días un bocadillo

if lunes:
    print("toca pizza")
elif jueves:
    print("toca paella")
else:
    print("toca bocadillo")

# Ejercicio: 
# Preguntar la edad al usuario
# si tiene menos de 12 años -> eres un niño/a
# si tiene menos de 18 -> eres un/a adolescente
# si tiene menos de 30 -> eres muy joven
# si tiene menos de 40 -> eres joven, pero menos
# si tiene más o igual a 40 -> tu puedes con todo

'''
edad = int(input("por favor, indica tu edad -> "))
# edad = int(edad)

if 0 <= edad < 12:
    print("eres un niño/a")
elif edad < 18:
    print("eres un/a adolescente")
elif edad < 30:
    print("eres muy joven")
elif edad < 40:
    print("eres joven, pero menos")
elif edad < 120 :
    print("tu puedes con todo")
else:
    print("no me lo creo")
'''

# Ejercicio: 
# Preguntar al usuario la edad
# si tiene menos de 0 o más de 120 diremos : no me lo creo
# si tiene menos de 18 diremos : aun no puedes votar, te faltan x años
# si tiene 18 o más, diremos : puedes votar desde hace x años

# Ejercicio
# pedir al usuario un número
# pedir otro número
# si no son números cada uno le diremos que no se puede hacer
# pedir qué operación matemática quiere hacer (7 posibilidades)
#     suma
#     resta
#     multi
#     division
#     exp
#     div_ent
#     modulo
# pero si no es ninguna de estas mostraremos un mensaje de error
# si divide por cero también mostraremos un mensaje
#
# Al final debe aparecer algo así :
# Escriba el primer número -> 1
# Escriba el segundo número ->3
# ¿Qué operación quiere realizar? suma
# 1 + 3 = 4












