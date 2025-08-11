import pygame # For import use "python3 -m pip install pygame"
import random


pygame.init()
clock = pygame.time.Clock()

# Fenêtre
LARGEUR, HAUTEUR = 640, 480
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Pong")

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)


centre = (LARGEUR-10)//2
border = 10


police = pygame.font.Font("ressource/font/PressStart2P.ttf", 20)

# Sons
player_pop = pygame.mixer.Sound("ressource/sound_effects/pop.mp3")
wall_pop = pygame.mixer.Sound("ressource/sound_effects/pop_wall.mp3")
loose_pop = pygame.mixer.Sound("ressource/sound_effects/pop_loose.mp3")
player_win = pygame.mixer.Sound("ressource/sound_effects/player_win.mp3")

# Variables temps
pause = False
pause_duree = 2000  # ms
pause_debut = 0

# Scores
player1_score = 0
player2_score = 0

# Balle
balle_x = LARGEUR // 2
balle_y = HAUTEUR // 2
balle_vx = 3.5
balle_vy = 0
balle_radius = 12
bonk = False



# Pad gauche (joueur 1)
pad1_x = 10
pad1_y = HAUTEUR // 2 - 40
pad1_largeur = 10
pad1_hauteur = 80
pad1_vitesse = 5

# Pad droit (joueur 2)
pad2_x = LARGEUR - 20
pad2_y = HAUTEUR // 2 - 40
pad2_largeur = 10
pad2_hauteur = 80
pad2_vitesse = 5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    if player1_score == 10: # Player 1 WIN
        pygame.draw.rect(screen, ROUGE, (centre, 0, 10, HAUTEUR))
        screen.blit(texte_win1, (LARGEUR //5 ,HAUTEUR//3))
        screen.blit(win, (LARGEUR //5 ,HAUTEUR//2.4))
        pygame.display.flip()
        player_win.play()

    elif player2_score == 10: # Player 2 WIN
        pygame.draw.rect(screen, ROUGE, (centre, 0, 10, HAUTEUR))
        screen.blit(texte_win2, (LARGEUR -240 ,HAUTEUR//3))
        screen.blit(win2, (LARGEUR - 240 ,HAUTEUR//2.4))
        pygame.display.flip()
        player_win.play()

    else:
        touches = pygame.key.get_pressed()

        # Déplacement pad joueur 1
        if touches[pygame.K_z]:
            pad1_y -= pad1_vitesse

        if touches[pygame.K_s]:
            pad1_y += pad1_vitesse
            
        # Déplacement pad joueur 2
        if touches[pygame.K_UP]:
            pad2_y -= pad2_vitesse

        if touches[pygame.K_DOWN]:
            pad2_y += pad2_vitesse

        # Empêcher sortie écran
        pad1_y = max(0, min(HAUTEUR - pad1_hauteur, pad1_y))
        pad2_y = max(0, min(HAUTEUR - pad2_hauteur, pad2_y))

        
        if not pause:

            balle_x += balle_vx
            balle_y += balle_vy

            # Rebond haut/bas
            if balle_y - balle_radius <= 0 or balle_y + balle_radius >= HAUTEUR:
                balle_vy *= -1
                wall_pop.play()

            # Collision pad gauche
            if pad1_x <= balle_x  <= pad1_x + pad1_largeur and pad1_y <= balle_y <= pad1_y + pad1_hauteur :
                balle_vx *= -1
                player_pop.play()
                if  balle_y - pad1_y < pad1_hauteur/2  : # HAUT
                    balle_vy -= random.randint(1,2)
                elif balle_y - pad1_y > pad1_hauteur/2: # BAS
                    balle_vy += random.randint(1,2)
                if  bonk == False:
                    balle_vx *= 1.8
                    bonk = True

            # Collision pad droit
            if pad2_x <= balle_x  <= pad2_x + pad2_largeur and pad2_y <= balle_y <= pad2_y + pad2_hauteur :
                balle_vx *= -1
                player_pop.play()

                if  balle_y - pad2_y < pad2_hauteur/2  : # HAUT
                    balle_vy -= random.randint(1,2)
                elif balle_y - pad2_y > pad2_hauteur/2: # BAS
                    balle_vy += random.randint(1,2)
                if  bonk == False:
                    balle_vx *= 1.8
                    bonk = True
            

            # Point pour joueur 2
            if balle_x - balle_radius <= 0:
                player2_score += 1
                loose_pop.play()
                pause = True
                pause_debut = pygame.time.get_ticks()


            # Point pour joueur 1
            if balle_x + balle_radius >= LARGEUR:
                player1_score += 1
                loose_pop.play()
                pause = True
                pause_debut = pygame.time.get_ticks()

        else:
            # Si pause terminée (non bloquante)
            if pygame.time.get_ticks() - pause_debut >= pause_duree:
                pause = False
                
                balle_x = LARGEUR // 2
                balle_y = HAUTEUR // 2
                
                balle_vx = -3.5 if balle_vx < 0 else 3.5

                balle_vy = 0
                bonk = False
                

        texte_score_player1 = police.render(f"{player1_score}", True, (255, 255, 255))
        texte_score_player2 = police.render(f"{player2_score}", True, (255, 255, 255))

        texte_win1 = police.render("Player 1", True, (255, 255, 255))
        win = police.render("WINS", True, (255, 255, 255))
        texte_win2 = police.render("Player 2", True, (255, 255, 255))
        win2 = police.render("WINS", True, (255, 255, 255))

        # Affichage
        screen.fill(NOIR)
        pygame.draw.rect(screen, BLANC, (pad1_x, pad1_y, pad1_largeur, pad1_hauteur))
        pygame.draw.rect(screen, BLANC, (pad2_x, pad2_y, pad2_largeur, pad2_hauteur))
        pygame.draw.rect(screen, ROUGE if pause else BLANC, (balle_x, balle_y , balle_radius, balle_radius))
        if player1_score >= 10 or player2_score >= 10:
            pygame.draw.rect(screen, NOIR , (centre, 0, 10, HAUTEUR))
        else: # Écran fin de partie
            pygame.draw.rect(screen, BLANC , (centre, 0, 10, HAUTEUR))
        screen.blit(texte_score_player1, (centre / (1.2) ,HAUTEUR//2))
        screen.blit(texte_score_player2, (centre *1.18 ,HAUTEUR//2))
        
 
        pygame.display.flip()
        clock.tick(60)

pygame.quit()