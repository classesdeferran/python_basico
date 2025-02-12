"""
EJERCICIO DICCIONARIOS

Tenemos un sitio que registra los accesos de los usuarios.

Necesitamos un menú con estas opciones
1. Añadiremos un usuario 
        (si no existe ya)
2. Añadiremos una visita al usuario indicado 
        (si el usuario no existe mostrar el error)
3. Mostraremos las visitas del usuario que se decida
        (si el usuario no existe mostrar el error)
4. Mostraremos las visitas de todos los usuarios
        (si no hay usuarios todavía indicarlo)
X. Salir

Consideraremos que el nombre de cada usuario es único

"""

import os
os.system("cls")

users = []
while True:
    menu = """
1. Añadiremos un usuario 
2. Añadiremos una visita al usuario indicado 
3. Mostraremos las visitas del usuario que se decida
4. Mostraremos las visitas de todos los usuarios
X. Salir
"""
    print(menu)
    opcion = input("Elige tu opcion --> ").strip().lower()

    match opcion:
        case "1":
            # Pido al usuario los datos
            new_user = input("Nuevo usuario --> ").strip().title()
            # verificamos si ya hay algún usuario en la lista
            if users:
                # si ya hay algún usuario en la lista
                # debemos verificar que no coincida con new_user
                users_name = [] # lista para guardar los nombres de los usuarios 
                for user in users:
                    # Obtenemos y guardamos los nmbres de los usarios
                    users_name.append(user['nombre'])

                # Si el nombre no está en la lista lo añadimos
                if new_user not in users_name:
                    user_dic = {"nombre":new_user, "visitas": 0 }
                    users.append(user_dic)
                    print(f"Usuario {new_user} añadido correctamente")
                else:
                    print("El usuario ya existe")
            else:
                user_dic = {"nombre":new_user, "visitas": 0 }
                users.append(user_dic)
                print(f"Usuario {new_user} añadido correctamente")
        case "2":       
            pass
        case "3":
            pass
        case "4":
            if users:
                print(users)
            else:
                print("No hay usuarios todavía")
        case "x":
            print("Fin del programa")
            break
        case _ :
            print("Opción no reconocida.\nVuélvelo a probar.")

print(users)

