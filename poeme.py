# Génératuer de "poèmes"
nombre = 0
valeur = None

def get_number ():
    global valeur
    valeur = int(input("choisi un nombre : "))



def print_colone(): 
    global nombre
    nombre += 1
    for i in range(nombre):
        print(f"{str(nombre).zfill(3)}" ,end="  ")
        
  
def print_poeme():
    while valeur > nombre:
        print_colone()
        print()

def game():
    get_number()
    print_poeme()
    
game()
# Build by Oraxelerator