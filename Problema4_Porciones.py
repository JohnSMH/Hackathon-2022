import math

def Porciones():
    print("Cuantos amigos son:")
    amigos = input()
    print("Cuantas porciones por amigo son:")
    porciones = input()
    total = int(amigos) * int(porciones)
    pasteles = math.ceil(total / 4)
    print("Se necesitan ", pasteles, " pasteles")

Porciones()

