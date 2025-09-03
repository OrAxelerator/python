import random
# Programme écrit le 5 janvier 2025..

valeur = 0
valeur_cache = 0 
x = 1
question = None
m = 0

def get_difficulte () : # Obtenir difficulté
    difficulte = input("choisi ta difficulé : "  )
    if difficulte == "a" :
      global liste
      liste  = [1 , 33]
    if difficulte == "c" :
      liste = [1 ,200]
    elif difficulte != "a" and "b" and "c" :
      print("----------------------------------")
      print("choisi une valeur correct idiot ")
      get_difficulte()

def game(x) : # Lance le jeu
  x += 1
  print("----------------------------------")
  print("Difficultés ?" )
  print("a = facile")
  print("c = difficile")
  print("----------------------------------") 
  

  get_difficulte()  #s'execute tout seul
  global valeur_cache
  valeur_cache = random.randint(liste[0], liste[1])
  int(valeur_cache)
  valeur = 0
  valeur_signe = 0
  print("----------------------------------")
  print("BUT DU JEU :")
  print("trouver le  chiffre secret")
  print("La console vous donnera des indices")
  print("----------------------------------")


  while  valeur != valeur_cache :
    verifier_signe(valeur_signe)


def verifier_signe(valeur_signe):
    global valeur
    valeur = int(input("valeur :  "))
    valeur_signe = valeur_cache - valeur
    if valeur_signe > 0:
        if 0 < valeur_signe < 30 :
            print("----------------------------------")
            print("petite augmentation mon reuf ")
            print("----------------------------------")
        else : 
            print("----------------------------------")
            print("il faut une grande augmentation chef ") 
            print("----------------------------------")
    elif valeur_signe < 0:
        if -30 < valeur_signe < 0 :
          print("----------------------------------")
          print("petit diminution")
          print("----------------------------------")
        else :
            print("----------------------------------")
            print("grande diminution requise ")
            print("----------------------------------")
    if valeur == valeur_cache :
      print("----------------------------------")
      print("Bravo le chiffre secret était " + str(valeur_cache))
      global x
      x += 1
      global question
      question = "?" * x
      print("écrit 'oui' ")
      relance = input( str(x) +  " ème manche " + str(question) )
      if relance == "oui" :
        game(x)
      else :
        print("----------------------------------")
        print("fin du programme ")
        global m
        m += 1
        return
        

if m == 0 :
    game(x)
else :
    print("----------------------------------")
    print("fin du programme ")
    pass

# OrAxelerator 