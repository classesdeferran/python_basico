"""
WHILE = mientras
"""

num = 5
while num > 0:  
    print(num)
    num -= 1
else:
    print("Has entrado en el else")

print("#" * 20)
num = 5
while True:  
    print(num)
    num -= 1
    if num == 0:
        break
else:
    print("Has entrado en el else")

monedas = 10
while True:
    prestamo = input("¿Cuantas monedas necesitas? ")