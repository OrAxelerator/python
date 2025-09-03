import string
import random
import tkinter as tk
import subprocess
import os
import subprocess

# Programme écrit le 9 janiver

i = None

fin = "------------------------------------"

difficulté1 = string.ascii_letters
difficulté2 = difficulté1 +  string.digits
difficulté3 = difficulté2 + string.punctuation
difficulté = None

longuer = 3
mot_de_passe = "A"
reel_passe = mot_de_passe[1:]
re_start = None

RED = '\033[31m'
RESET = '\033[0m'  # Réinitialiser la couleur par défaut


texte = "mot2passe.txt"
nom = None

def get_difficulté():
    global difficulté
    valeur = input("rentre ta difficulté : ")
    if valeur == "1":
        difficulté = difficulté1
    elif valeur == "2":
        difficulté = difficulté2
    elif valeur == "3":
        difficulté = difficulté3
    else :
        print("valeur pas comprise entre 1 et 3, recommence")
        get_difficulté()


def get_longueur():
    longuer = input("Rentre la longueur do mot de passe : ")

    if longuer == "0":
        print("Un mot de passe à 0 caractère, t'es un génie lol.")
        return get_longueur()

    if not longuer.isdigit():
        print("Problème : l'entrée contient autre chose que des chiffres. Recommence.")
        return get_longueur()

    print("C'est bon, l'entrée est valide.")
    return int(longuer) 

def ouvrir():
    subprocess.run(["open", "mot2passe.txt"])

def create_mot_de_passe():
    global mot_de_passe
    global reel_passe
    mot_de_passe = reel_passe
    for i in range(int(valeur)):
        mot_de_passe = str(mot_de_passe) + str(random.choice(difficulté))




def gerer_fichier(chemin_du_fichier, contenu):
    try:
        # Ouvrir le fichier en mode ajout ('a') pour ne pas écraser le contenu existant
        with open(chemin_du_fichier, 'a') as fichier:
            fichier.write('\n'+ '\n' + contenu)  # Ajouter un saut de ligne avant d'ajouter le contenu
        print(f"Le contenu a été ajouté dans le fichier : {chemin_du_fichier}")
        
        # Ouvrir automatiquement le fichier dans l'application par défaut (comme TextEdit sur macOS)
        subprocess.run(["open", chemin_du_fichier])  # Pour macOS
        # subprocess.run(["notepad", chemin_du_fichier])  # Pour Windows
        
        # Attendre que l'utilisateur ferme l'éditeur
       # print("L'éditeur a été fermé. Le fichier est enregistré et fermé.")
    
    except Exception as e:
        print(f"Erreur lors de l'accès au fichier : {e}")


def questioner():
    global re_start
    print(fin)
    print("que faire ?")
    print("a = enregistrer mot de passe")
    print("z = re-generer mot de passe")
    print("e = recommencer opération")
    print("r = ouvrir répertoire mot de passe et fermer programme")
    re_start = input( "   :  ")

def choix():
    print(f' voici le mot de passe générer : {RED}{mot_de_passe}{RESET}')
    questioner()
    if re_start == "a":
        nom = input("nom du mot de passe ? : ")
        gerer_fichier("mot2passe.txt" , nom + " : " + mot_de_passe)
    elif re_start == "z":
        create_mot_de_passe()
        choix()
    elif re_start == "e":
        main()
    elif re_start == "r":
        ouvrir()
    else :
        print("rentre valeur correct")
        choix()


def main():
    global valeur
    global texte
    global nom
    print(fin)
    get_difficulté()
    print(fin)
    valeur = get_longueur()
    print(fin)
    create_mot_de_passe()
    choix()

print(fin)
print("a = ouvrir répertoire mot de passe ")
print("'autre' =créer nouveau mot de passe ")
regarder = input(":")
if regarder == "a":
    ouvrir()
else :
    main()


print("fin du programme")
# Design by OrAxelerator