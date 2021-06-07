import sys
import pygame

class Jeu:
    def __init__(self, screen):
        self.screen = screen
        self.accueil = True
        self.screen_debut = False
        self.screen_regle = False

        self.image = pygame.image.load("./Menu/abalone.png")
        self.image_modif = pygame.transform.scale(self.image, (150, 150))

        # l'image bouton
        self.bouton = pygame.image.load('./Menu/play.png')
        self.bouton = pygame.transform.scale(self.bouton, (200, 100))
        self.bouton_coord = self.bouton.get_rect()
        self.bouton_coord.x = 320
        self.bouton_coord.y = 450

        self.parametre = pygame.image.load('./Menu/parametre.png')
        self.parametre = pygame.transform.scale(self.parametre, (80, 80))

        # l'image suivant (regle)
        self.suivant = pygame.image.load("./Menu/suivant.png")
        self.suivant = pygame.transform.scale(self.suivant, (50, 50))
        self.suivant_coord = self.suivant.get_rect()
        self.suivant_coord.x = 700
        self.suivant_coord.y = 700

        # l' image regle
        self.regle = pygame.image.load("./Menu/rule.png")


        # image bouton jouer (configuration)
        self.img_livre = pygame.image.load("Menu/rule.png")
        self.img_livre = pygame.transform.scale(self.img_livre, (50, 50))
        self.jouer = pygame.image.load('./Menu/play.png')
        self.jouer = pygame.transform.scale(self.jouer, (200, 100))
        self.jouer_coord = self.jouer.get_rect()
        self.jouer_coord.x = 320
        self.jouer_coord.y = 680

        # image de fond screen
        self.fond = pygame.image.load("./Menu/fond.jpg")
        self.fond = pygame.transform.scale(self.fond, self.screen.get_size())

        self.liste_configuration = ["Standard", "Domanation", "Face à Face", "Fujiyama", "Infiltration",
                                   "Marguerite allemande", "Marguerite belge", "Marguerite Hollandaise",
                                   "Marguerite suisse", "Pyramide", "Snake variante", "Personnalisé"]
        self.liste_joueur = ["1", "2", "3", "4"]

    def master(self):

        while self.accueil:
            self.screen.blit(self.fond, (0, 0))
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
                if evenement.type == pygame.MOUSEBUTTONDOWN and self.bouton_coord.collidepoint(evenement.pos):
                    self.accueil = False
                    self.screen_regle = True
                self.message("grande", "WELCOME TO ABALONE ", (30, 220, 100, 50), (255, 255, 255))
<<<<<<< HEAD
                self.screen.blit(self.image_modif, (350, 280, 100, 50))
                self.screen.blit(self.button, self.button_play)
=======
                self.ecran.blit(self.image_modif, (350, 280, 100, 50))
                self.ecran.blit(self.bouton, self.bouton_coord)
>>>>>>> 5893c9e315cbc863776b13b5543a9b052c304bfc
                pygame.display.flip()

        while self.screen_regle:
            self.screen.blit(self.fond, (0, 0))
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
<<<<<<< HEAD
                if evenement.type == pygame.MOUSEBUTTONDOWN and self.suivant_play.collidepoint(evenement.pos):
                    self.screen_regle = False
                    self.screen_debut = True
                self.message("moyenne", "Règles", (300, 50, 100, 50), (255, 255, 255))
                self.screen.blit(self.suivant, self.suivant_play)
                self.screen.blit(self.rule, (460, 48, 100, 50))
                self.screen.blit(self.regle, (15, 120, 100, 50))
=======
                if evenement.type == pygame.MOUSEBUTTONDOWN and self.suivant_coord.collidepoint(evenement.pos):
                    self.ecran_regle = False
                    self.ecran_debut = True
                self.message("moyenne", "Règles", (300, 50, 100, 50), (255, 255, 255))
                self.ecran.blit(self.suivant, self.suivant_coord)
                self.ecran.blit(self.img_livre, (460, 48, 100, 50))
                self.ecran.blit(self.regle, (15, 120, 100, 50))
>>>>>>> 5893c9e315cbc863776b13b5543a9b052c304bfc
                pygame.display.flip()

        while self.screen_debut:
            self.screen.blit(self.fond, (0, 0))
            pygame.draw.rect(self.screen,(157,99,61,255), (15, 120, 768, 550))
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
                self.message("moyenne", "Configuration", (160, 50, 100, 50), (255, 255, 255))
                self.message("petite", "Number of players", (350, 140, 100, 50), "black")
                self.message("petite", "configuration table", (350, 300, 100, 50), "black")
<<<<<<< HEAD
                self.screen.blit(self.jouer, self.jouer_play)
                self.screen.blit(self.parametre, (550, 30, 100, 50))
=======
                self.ecran.blit(self.jouer, self.jouer_coord)
                self.ecran.blit(self.parametre, (550, 30, 100, 50))
>>>>>>> 5893c9e315cbc863776b13b5543a9b052c304bfc

                # checkbox for player
                k = 0
                for i in range(0, 300, 60):
<<<<<<< HEAD
                    pygame.draw.rect(self.screen, "WHITE", (340 + i, 200, 15, 15))
                    self.message("petite", self.list_player[k], (341 + i, 220, 100, 50), "black")
=======
                    pygame.draw.rect(self.ecran, "WHITE", (340 + i, 200, 15, 15))
                    self.message("petite", self.liste_joueur[k], (341 + i, 220, 100, 50), "black")
>>>>>>> 5893c9e315cbc863776b13b5543a9b052c304bfc
                    k += 1
                    if k == len(self.liste_joueur):
                        break

                # checkbox for table
                k = 0
                for i in range(0, 600, 300):
                    for j in range(0, 300, 50):
<<<<<<< HEAD
                        pygame.draw.rect(self.screen, "WHITE", (200 + i, 363 + j, 15, 15))
                        self.message("petite", self.list_configuration[k], (220 + i, 360 + j, 100, 50), "black")
=======
                        pygame.draw.rect(self.ecran, "WHITE", (200 + i, 363 + j, 15, 15))
                        self.message("petite", self.liste_configuration[k], (220 + i, 360 + j, 100, 50), "black")
>>>>>>> 5893c9e315cbc863776b13b5543a9b052c304bfc
                        k += 1
                        if k == len(self.liste_configuration):
                            break
<<<<<<< HEAD
                if evenement.type == pygame.MOUSEBUTTONDOWN and self.jouer_play.collidepoint(evenement.pos):
                    self.screen_debut = False
=======
                if evenement.type == pygame.MOUSEBUTTONDOWN and self.jouer_coord.collidepoint(evenement.pos):
                    self.ecran_debut = False
>>>>>>> 5893c9e315cbc863776b13b5543a9b052c304bfc
                pygame.display.flip()


    def message(self, font, message, message_rectangle, couleur):
        if font == "petite":
            font = pygame.font.SysFont('Times New Roman', 20, False)
        elif font == "moyenne":
            font = pygame.font.SysFont('castellar', 40, False)

        elif font == "grande":
            font = pygame.font.SysFont('castellar', 50, True)
        message = font.render(message, True, couleur)
        self.screen.blit(message, message_rectangle)

