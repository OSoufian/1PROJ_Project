import sys
import pygame

class Jeu:
    def __init__(self):
        self.ecran = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Abalone")
        self.accueil = True
        self.ecran_debut = False
        self.ecran_regle = False

        self.image = pygame.image.load("./Menu/abalone.png")
        self.image_modif = pygame.transform.scale(self.image, (150, 150))

        # l'image bouton
        self.button = pygame.image.load('./Menu/play.png')
        self.button = pygame.transform.scale(self.button, (200, 100))
        self.button_play = self.button.get_rect()
        self.button_play.x = 320
        self.button_play.y = 450

        self.parametre = pygame.image.load('./Menu/parametre.png')
        self.parametre = pygame.transform.scale(self.parametre, (80, 80))

        # l'image suivant (regle)
        self.suivant = pygame.image.load("./Menu/suivant.png")
        self.suivant = pygame.transform.scale(self.suivant, (50, 50))
        self.suivant_play = self.suivant.get_rect()
        self.suivant_play.x = 700
        self.suivant_play.y = 700

        # l' image regle
        self.regle = pygame.image.load("./Menu/regle.png")
        

        # image bouton jouer (configuration)
        self.rule = pygame.image.load("Menu/rule.png")
        self.rule = pygame.transform.scale(self.rule, (50, 50))
        self.jouer = pygame.image.load('./Menu/play.png')
        self.jouer = pygame.transform.scale(self.jouer, (200, 100))
        self.jouer_play = self.jouer.get_rect()
        self.jouer_play.x = 320
        self.jouer_play.y = 680

        # image de fond ecran
        self.fond = pygame.image.load("./Menu/fond.jpg")
        self.fond = pygame.transform.scale(self.fond, self.ecran.get_size())

        self.list_configuration = ["Standard", "Domanation", "Face à Face", "Fujiyama", "Infiltration",
                                   "Marguerite allemande", "Marguerite belge", "Marguerite Hollandaise",
                                   "Marguerite suisse", "Pyramide", "Snake variante", "Personnalisé"]
        self.list_player = ["1", "2", "3", "4"]

    def master(self):

        while self.accueil:
            self.ecran.blit(self.fond, (0, 0))
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
                if evenement.type == pygame.MOUSEBUTTONDOWN and self.button_play.collidepoint(evenement.pos):
                    self.accueil = False
                    self.ecran_regle = True
                self.message("grande", "WELCOME TO ABALONE ", (30, 220, 100, 50), (255, 255, 255))
                self.ecran.blit(self.image_modif, (350, 280, 100, 50))
                self.ecran.blit(self.button, self.button_play)
                pygame.display.flip()

        while self.ecran_regle:
            self.ecran.blit(self.fond, (0, 0))
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
                if evenement.type == pygame.MOUSEBUTTONDOWN and self.suivant_play.collidepoint(evenement.pos):
                    self.ecran_regle = False
                    self.ecran_debut = True
                self.message("moyenne", "Règles", (300, 50, 100, 50), (255, 255, 255))
                self.ecran.blit(self.suivant, self.suivant_play)
                self.ecran.blit(self.rule, (460, 48, 100, 50))
                self.ecran.blit(self.regle, (15, 120, 100, 50))
                pygame.display.flip()

        while self.ecran_debut:
            self.ecran.blit(self.fond, (0, 0))
            pygame.draw.rect(self.ecran,(157,99,61,255), (15, 120, 768, 550))
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
                self.message("moyenne", "Configuration", (160, 50, 100, 50), (255, 255, 255))
                self.message("petite", "Number of players", (350, 140, 100, 50), "black")
                self.message("petite", "configuration table", (350, 300, 100, 50), "black")
                self.ecran.blit(self.jouer, self.jouer_play)
                self.ecran.blit(self.parametre, (550, 30, 100, 50))

                # checkbox for player
                k = 0
                for i in range(0, 300, 60):
                    pygame.draw.rect(self.ecran, "WHITE", (340 + i, 200, 15, 15))
                    self.message("petite", self.list_player[k], (341 + i, 220, 100, 50), "black")
                    k += 1
                    if k == len(self.list_player):
                        break

                # checkbox for table
                k = 0
                for i in range(0, 600, 300):
                    for j in range(0, 300, 50):
                        pygame.draw.rect(self.ecran, "WHITE", (200 + i, 363 + j, 15, 15))
                        self.message("petite", self.list_configuration[k], (220 + i, 360 + j, 100, 50), "black")
                        k += 1
                        if k == len(self.list_configuration):
                            break
                if evenement.type == pygame.MOUSEBUTTONDOWN and self.jouer_play.collidepoint(evenement.pos):
                    self.ecran_debut = False
                pygame.display.flip()


    def message(self, font, message, message_rectangle, couleur):
        if font == "petite":
            font = pygame.font.SysFont('Times New Roman', 20, False)
        elif font == "moyenne":
            font = pygame.font.SysFont('castellar', 40, False)

        elif font == "grande":
            font = pygame.font.SysFont('castellar', 50, True)
        message = font.render(message, True, couleur)
        self.ecran.blit(message, message_rectangle)

if __name__ == "__main__":
    pygame.init()
    Jeu().master()
    pygame.quit()
