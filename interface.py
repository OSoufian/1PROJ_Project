import typing
import pygame as pg
import platform
class CheckBox:
    
    def __init__(self, font: pg.font.Font, positions: typing.List[pg.Rect], labels: typing.List[str]):
        self.checked = 0
        self.positions = positions
        self.font = font
        self.list_surfaces = [font.render(text, False, "black") for text in labels]
        self.labels = list(labels)
    
    def draw(self, screen):
        i = 0
        for pos, label in zip(self.positions, self.list_surfaces):
            pg.draw.rect(screen, "white", pos)
            screen.blit(label, (pos.x + 40, pos.y))
            if i == self.checked:
                pg.draw.circle(screen, "black", pos.center, 10)
            i += 1
    
    def click(self, mouse_pos):
        i = 0
        for pos in self.positions:
            if pos.collidepoint(mouse_pos):
                self.checked = i
                return i
            i += 1

class Jeu:
    def __init__(self, screen):
        self.screen = screen   
        self.mod_player = None     
        self.image = pg.transform.scale(pg.image.load("./Menu/abalone.png"), (400, 500)).convert_alpha()
        self.parametre = pg.transform.scale(pg.image.load('./Menu/parametre.png'), (80, 80)).convert_alpha() # l'image paramètre (regle)     
        self.next = pg.transform.scale(pg.image.load("./Menu/suivant.png"), (50, 50)).convert_alpha() # l'image next (regle)
        self.regle = pg.image.load("./Menu/regle.png").convert_alpha() # l' image regle
        self.book_image = pg.transform.scale(pg.image.load("Menu/rule.png"), (50, 50)).convert_alpha() # image button play (configuration)
        self.play = pg.transform.scale(pg.image.load('./Menu/play.png'), (200, 100)).convert_alpha()       
        self.fond = pg.transform.scale(pg.image.load("./Menu/fond.jpg"), self.screen.get_size()).convert_alpha() # image de fond screen

        self.button_coord = self.play.get_rect(x=300, y=580)

        self.next_coord = self.next.get_rect(x=700, y=700)

        self.play_coord = self.play.get_rect(x=320, y=700)

        self.mode = ["Standard","Domination", "Face a Face", "Fujiyama", "Infiltration",
                "Marguerite allemande", "Marguerite belge", "Marguerite Hollandaise",
                "Marguerite suisse", "Pyramide", "Snakes", "The wall", "Alliances", "Araignee",
                "Forcage", "Centrifugeuse", "Mosaique", "Personnalise"]

    def master(self):
        conditonal = 0
        check_player = CheckBox(pg.font.SysFont('Times New Roman', 20), [pg.Rect(200 + i * 100, 200, 20, 20) for i in range(7)], [f"{i}" for i in range(2, 7)])
        check_standard = CheckBox(pg.font.SysFont('Times New Roman', 20), [pg.Rect(50, 350, 20, 20)], ("Standard",))
        check_mode = CheckBox(pg.font.SysFont('Times New Roman', 20), [pg.Rect(50 + (500 if i >= 12 else (250 if i >= 6 else 0)), 350 + i * 50 % 300, 20, 20) for i in range(18)], (f"{i}" for i in self.mode))
        while conditonal < 3:

            self.screen.blit(self.fond, (0,0))

            for evenement in pg.event.get():   
                if pg.QUIT == evenement.type: pg.quit()    
                if evenement.type == pg.MOUSEBUTTONDOWN and self.button_coord.collidepoint(evenement.pos):
                    conditonal += 1
                if evenement.type == pg.MOUSEBUTTONDOWN:
                    check_player.click(evenement.pos)
                    check_mode.click(evenement.pos)

                # welcome page
                elif conditonal == 0:

                    self.message("moyenne", "WELCOME TO ABALONE", (160, 80, 100, 50), (255, 255, 255))
                    self.screen.blit(self.image, (190, 100, 100, 50)) and self.screen.blit(self.play, self.button_coord)
                    pg.display.flip()

                # rules page
                elif conditonal == 1:

                    self.message("moyenne", "Règles", (300, 50, 100, 50), (255, 255, 255))
                    self.screen.blit(self.next, self.next_coord) and self.screen.blit(self.book_image, (460, 48, 100, 50))
                    self.screen.blit(self.regle, (15, 120, 100, 50))
                    self.button_coord = self.next_coord
                    pg.display.flip()

                # play page
                else:
                    self.button_coord = self.play_coord
                    self.screen.blit(self.fond, (0, 0))
                    pg.draw.rect(self.screen, (157, 99, 61, 255), (15, 120, 768, 550))
                    self.message("moyenne", "Configuration", (160, 50, 100, 50), (255, 255, 255))
                    self.message("petite", "Number of players", (340, 140, 100, 50), "black")
                    self.message("petite", "configuration table", (340, 300, 100, 50), "black")
                    self.screen.blit(self.play, self.play_coord)
                    self.screen.blit(self.parametre, (550, 30, 100, 50))
                    check_player.draw(self.screen)
                    if check_player.checked > 0:
                        check_standard.draw(self.screen)
                    else:
                        check_mode.draw(self.screen)
                    pg.display.flip()
            self.mod_player= self.mode[check_mode.checked], check_player.labels[check_player.checked]
            
    def message(self, police, message, message_rectangle, couleur):
        if police == "petite":
            police = pg.font.SysFont('Times New Roman', 20, False)
        elif police == "moyenne":
            police = pg.font.SysFont('castellar', 40, False)
        elif police == "grande":
            police = pg.font.SysFont('castellar', 50, True)
        message = police.render(message, True, couleur)
        self.screen.blit(message, message_rectangle)