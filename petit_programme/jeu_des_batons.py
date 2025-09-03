import random
# Programme écrit le 9 janvier 2025


number_of_stick = 20
play = 0
baton = ["  |  "  ]
value = None

a = None
b = None
players = []
x = 0
revanche = 0

fin = "---------------------------"

def regle():# Print les regles du jeu
    print(fin)
    print("RÈGLE DU JEU :")
    print("dans ce jeu 2 joueur s'affrontent ")
    print("le but est de ne pas etre la personne a prendre le dernier baton")
    print("vous pouvez prendre 1 , 2 , 3 ou 4 batton par tour ")
    print("pour savoir qui commence, c'est le programme qui décide")
    print("entrer les noms des 2 joueurs.")
    print(fin)


def player(x):# Selectionnez pseudos
    global a
    global b
    global players
    if x == 0:
        a = input("entrer nom du joueur A : ")
        b = input("entrer nom du joueur B : ")
        if a == b :
            print("les 2 joueur peuvent pas avoir le même nom XD")
            player(0)
        players = [a , b]
    random.shuffle(players)
    print(fin)
    print(players[0] + " sera le joueur 1 ")
    print(players[1] + " sera le joueur 2")
    #print(players)
    print(fin)


def print_stick():# Print les batons
    global number_of_stick
    for _ in range(5):
        print("".join(map(str, baton * number_of_stick)))


def player_x_play() : 
    if play % 2 == 0 :
        print("c'est a " + players[0] + " de jouer")
    else :
        print("c'est au tour de " + players[1] + " de jouer")
    #print(players)


def player_x_last_play() : # Savoir qui joue en fin de parti et déclare le gagnat
    if play % 2 == 0 :
        print(fin)
        print("BRAVO " + players[0] + ", tu as gagné, " + players[1] + " te dois 5$ ")
    else :
        print(fin)
        print("BRAVO " + players[1] +", tu as gagné, " + players[0] + " te dois 5$ ")   
    #print(players)


def entré() :
    global value
    value = input("tu veux prendre combien de batons ? " )#####mettre pesudo joueur ?
    if int(value) >= 5 :
            print("prends une valeur pas supérieur a 4 mon reuf")
            entré()
    if int(value) <= 0 :
        print("prends pas une  valeur inférieur ou égal a 0 mon reuf")
        entré()
    else :
        return(value)


def game() :
    global number_of_stick
    global play
    global revanche
    print_stick()
    player_x_play()
    entré()
    play += 1
    number_of_stick -= int(value)
    if number_of_stick > 0 :
        game()
    else :
        player_x_last_play()
        print("revanche ??")
        revanche = input("'oui' pour validez : " )
        if revanche == "oui" :
            new_code()
        else :
            print("Pourquoi :(  ?")


def code() :
    regle()
    player(0)
    game()


def new_code():
    global number_of_stick
    number_of_stick = 20
    global play
    play = 0
    player(1)
    game()


code()

print("fin du programme")
# Design by OrAxelerator