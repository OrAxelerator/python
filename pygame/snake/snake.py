import pygame #for exe this file you need pygame, install it with : "pip install pygame"
import random
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
LARGEUR, HAUTEUR = 800, 600
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Snake")

# Couleurs
NOIR  = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT  = (0, 200, 0)
GRIS  = (50, 50, 50)

# Grille
taille_case    = 25
nombre_colone  = LARGEUR // taille_case
nombre_ligne   = HAUTEUR // taille_case

# Surface grille (pré-dessinée)
grid_surface = pygame.Surface((LARGEUR, HAUTEUR))
for x in range(0, LARGEUR, taille_case):
    pygame.draw.line(grid_surface, GRIS, (x, 0), (x, HAUTEUR))
for y in range(0, HAUTEUR, taille_case):
    pygame.draw.line(grid_surface, GRIS, (0, y), (LARGEUR, y))

# Initialisation du serpent (au centre)
start_x = (nombre_colone // 2) * taille_case
start_y = (nombre_ligne // 2) * taille_case
serpent = [(start_x, start_y)]
dx, dy = 0, 0  # direction initiale
taille = 1

# Pomme
def nouvelle_pomme():
    return (
        random.randint(0, nombre_colone - 1) * taille_case,
        random.randint(0, nombre_ligne - 1) * taille_case
    )

pomme_x, pomme_y = nouvelle_pomme()

# Horloge
clock = pygame.time.Clock()
FPS = 10

running = True
while running:
    clock.tick(FPS)

    # --- Gestion événements ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -taille_case, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = taille_case, 0
            elif event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -taille_case
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, taille_case
    print(serpent[0])
    # --- Mise à jour du serpent ---
    if dx != 0 or dy != 0:
        # Nouvelle tête
        new_head = (serpent[0][0] + dx, serpent[0][1] + dy)

        # Collision murs
        if (new_head[0] < 0 or new_head[0] >= LARGEUR or
            new_head[1] < 0 or new_head[1] >= HAUTEUR):
            print("Game Over ! Collision avec un mur.")
            running = False
        
        #if new_head[0] > LARGEUR :
         #   new_head = (LARGEUR,  serpent[0][1] + dy)  
        #if new_head[0] < 0:
         #   new_head = (0,  serpent[0][1] + dy)  

        
        # Collision avec soi-même
        if new_head in serpent:
            print("Game Over ! Collision avec soi-même.")
            running = False

        # Ajouter la tête
        serpent.insert(0, new_head)

        # Vérifier si la pomme est mangée
        if new_head == (pomme_x, pomme_y):
            taille += 1
            pomme_x, pomme_y = nouvelle_pomme()
        else:
            # Supprimer la queue si pas mangé
            serpent.pop()

    # --- Affichage ---
    screen.fill(NOIR)
    screen.blit(grid_surface, (0, 0))

    # Serpent
    # Serpent avec tête d'une couleur différente
    for i, (x, y) in enumerate(serpent):
        if i == 0:
        # tête
            pygame.draw.rect(screen, (120, 255, 140), (x, y, taille_case, taille_case))
        else:
        # corps
            pygame.draw.rect(screen, VERT, (x, y, taille_case, taille_case))


    # Pomme
    pygame.draw.rect(screen, ROUGE, (pomme_x, pomme_y, taille_case, taille_case))

    pygame.display.flip()

pygame.quit()
sys.exit()
