import pygame 
import random

pygame.init()
clock = pygame.time.Clock()

LARGEUR, HAUTEUR = 640, 480
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Pong")

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

centre = (LARGEUR-10)//2
border = 10

# Variables temps
pause = False
pause_duree = 2000  # ms
pause_debut = 0

class Pad:
    def __init__(self, x, y, largeur=10, hauteur=80, vitesse=5):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse = vitesse

    def draw(self, screen, couleur=BLANC):
        pygame.draw.rect(screen, couleur, (self.x, self.y, self.largeur, self.hauteur))

    def move_up(self):
        self.y -= self.vitesse

    def move_down(self):
        self.y += self.vitesse

    def collide(self, balle):
        if self.x <= balle.x <= self.x + self.largeur and self.y <= balle.y <= self.y + self.hauteur:
            balle.bonk_x()

            # Modifier la vitesse Y selon où ça tape
            if balle.y - self.y < self.hauteur/2:  # Haut du pad
                balle.vy -= random.randint(1, 2)
            elif balle.y - self.y > self.hauteur/2:  # Bas du pad
                balle.vy += random.randint(1, 2)

            # Premier rebond → accélération
            if balle.firstBonk is False:
                balle.vx *= 1.8
                balle.firstBonk = True

class Balle:
    def __init__(self, x=LARGEUR//2, y=HAUTEUR//2, vx=3.5, vy=0, radius=12, firstBonk=False):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.firstBonk = firstBonk

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen, pause=False):
        couleur = ROUGE if pause else BLANC
        pygame.draw.rect(screen, couleur, (self.x, self.y, self.radius, self.radius))

    def bonk_x(self): 
        self.vx *= -1
        player_pop.play()

    def bonk_y(self):
        self.vy *= -1
        wall_pop.play()

class Player:
    def __init__(self, score=0, vie=3):
        self.score = score
        self.vie = vie

    def sound_win(self):
        player_win.play()
    
    def sound_lost(self):
        loose_pop.play()

balle = Balle()
pad1 = Pad(x=10, y=HAUTEUR//2 - 40)
pad2 = Pad(x=LARGEUR-20, y=HAUTEUR//2 - 40)
player1 = Player()
player2 = Player()

police = pygame.font.Font("ressource/font/PressStart2P.ttf", 20)
texte_win1 = police.render("Player 1", True, (255, 255, 255))
win = police.render("WINS", True, (255, 255, 255))
texte_win2 = police.render("Player 2", True, (255, 255, 255))
win2 = police.render("WINS", True, (255, 255, 255))

# Sons
player_pop = pygame.mixer.Sound("ressource/sound_effects/pop.mp3")
wall_pop = pygame.mixer.Sound("ressource/sound_effects/pop_wall.mp3")
loose_pop = pygame.mixer.Sound("ressource/sound_effects/pop_loose.mp3")
player_win = pygame.mixer.Sound("ressource/sound_effects/player_win.mp3")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    if player1.score >= 10: # Player 1 WIN
        screen.fill(NOIR)
        pygame.draw.rect(screen, ROUGE, (centre, 0, 10, HAUTEUR))
        screen.blit(texte_win1, (LARGEUR //5 ,HAUTEUR//3))
        screen.blit(win, (LARGEUR //5 ,HAUTEUR//2.4))
        pygame.display.flip()
        player1.sound_win()
        pygame.time.delay(3000)
        running = False

    elif player2.score >= 10: # Player 2 WIN
        screen.fill(NOIR)
        pygame.draw.rect(screen, ROUGE, (centre, 0, 10, HAUTEUR))
        screen.blit(texte_win2, (LARGEUR -240 ,HAUTEUR//3))
        screen.blit(win2, (LARGEUR - 240 ,HAUTEUR//2.4))
        pygame.display.flip()
        player2.sound_win()
        pygame.time.delay(3000)
        running = False

    else:
        touches = pygame.key.get_pressed()

        # Déplacement pad joueur 1
        if touches[pygame.K_z]:
            pad1.move_up()
        if touches[pygame.K_s]:
            pad1.move_down()
            
        # Déplacement pad joueur 2
        if touches[pygame.K_UP]:
            pad2.move_up()
        if touches[pygame.K_DOWN]:
            pad2.move_down()

        # Empêcher sortie écran
        pad1.y = max(0, min(HAUTEUR - pad1.hauteur, pad1.y))
        pad2.y = max(0, min(HAUTEUR - pad2.hauteur, pad2.y))

        if not pause:
            balle.update()

            # Rebond haut/bas
            if balle.y - balle.radius <= 0 or balle.y + balle.radius >= HAUTEUR:
                balle.bonk_y()

            pad1.collide(balle)
            pad2.collide(balle)

            # Point pour joueur 2
            if balle.x - balle.radius <= 0:
                player2.score += 1
                player1.sound_lost()
                pause = True
                pause_debut = pygame.time.get_ticks()

            # Point pour joueur 1
            if balle.x + balle.radius >= LARGEUR:
                player1.score += 1
                player2.sound_lost()
                pause = True
                pause_debut = pygame.time.get_ticks()

        else:
            # Si pause terminée
            if pygame.time.get_ticks() - pause_debut >= pause_duree:
                pause = False
                balle.x = LARGEUR // 2
                balle.y = HAUTEUR // 2
                balle.vx = 3.5 * (-1 if random.random() < 0.5 else 1)
                balle.vy = 0
                balle.firstBonk = False

        # Affichage
        screen.fill(NOIR)
        pad1.draw(screen)
        pad2.draw(screen)
        balle.draw(screen, pause)

        # Barre centrale
        pygame.draw.rect(screen, BLANC, (centre, 0, 10, HAUTEUR))

        # Scores
        texte_score_player1 = police.render(f"{player1.score}", True, BLANC)
        texte_score_player2 = police.render(f"{player2.score}", True, BLANC)
        screen.blit(texte_score_player1, (centre / 1.2, HAUTEUR//2))
        screen.blit(texte_score_player2, (centre *1.18, HAUTEUR//2))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
