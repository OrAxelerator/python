# Génératuer de "poèmes"

def get_number ():
    valeur = int(input("choisi un nombre : "))
    return valeur


def print_colone(): 
    global nombre
    nombre += 1
    for i in range(nombre):
        print(f"{str(nombre).zfill(3)}" ,end="  ")


def print_poeme():
    while valeur > nombre:
        print_colone()
        print()

nombre = 0
valeur = get_number()
print_poeme()