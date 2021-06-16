import sys
import pygame as pg
import os


class Jeu:
    def __init__(self, screen, x, y, idnum, caption="", text_shift=(20, 1)):
        self.screen = screen
        pg.display.set_caption("Abalone")
        
        self.image = pg.transform.scale(pg.image.load("./Menu/abalone.png"), (400, 500))
        self.parametre = pg.transform.scale(pg.image.load('./Menu/parametre.png'), (80, 80)) # l'image paramètre (regle)     
        self.next = pg.transform.scale(pg.image.load("./Menu/suivant.png"), (50, 50)) # l'image next (regle)
        self.regle = pg.image.load("./Menu/regle.png") # l' image regle
        self.book_image = pg.transform.scale(pg.image.load("Menu/rule.png"), (50, 50)) # image button play (configuration)
        self.play = pg.transform.scale(pg.image.load('./Menu/play.png'), (200, 100))        
        self.fond = pg.transform.scale(pg.image.load("./Menu/fond.jpg"), self.screen.get_size()) # image de fond screen

        self.button_coord = self.play.get_rect()
        self.button_coord.x, self.button_coord.y = 300, 480

        self.next_coord = self.next.get_rect()
        self.next_coord.x= self.next_coord.y = 700

        self.play_coord = self.play.get_rect()
        self.play_coord.x, self.play_coord.y = 320, 680 

        self.configuration_list = ["Standard", "Domanation", "Face à Face", "Fujiyama", "Infiltration",
                                    "Marguerite allemande", "Marguerite belge", "Marguerite Hollandaise",
                                    "Marguerite suisse", "Pyramide", "Snake variante", "Personnalisé"]
        self.gamer_list = ["1", "2", "3", "4"]

        # attributs pour les checkbox
        self.x, self.y = x, y
        self.caption = caption
        self.text_shift = text_shift
        self.idnum = idnum
        self.box = pg.Rect(self.x, self.y, 12, 12)
        self.box_outline = self.box.copy()
        self.check = False

    def button_text(self):
        self.police = pg.font.SysFont('Ariel Black', 22)
        self.font_surf = self.police.render(self.caption, True, (0, 0, 0))
        w, h = self.police.size(self.caption)
        self.font_pos = (self.x + self.text_shift[0], self.y + 12 / 2 - h / 2 +
                         self.text_shift[1])
        self.screen.blit(self.font_surf, self.font_pos)

    def render_box(self):
        if self.check:
            pg.draw.rect(self.screen, (230, 230, 230), self.box)
            pg.draw.rect(self.screen, (0, 0, 0), self.box_outline, 1)
            pg.draw.circle(self.screen, (0, 0, 0), (self.x + 6, self.y + 6), 4)

        elif not self.check:
            pg.draw.rect(self.screen, (230, 230, 230), self.box)
            pg.draw.rect(self.screen, (0, 0, 0), self.box_outline, 1)
        self.button_text()

    def update(self, event_object):
        x, y = pg.mouse.get_pos()
        px, py, w, h = self.box
        if px < x < px + w and py < y < py + w:
            self.check = not self.check

    def update_box(self, event_object):
        if event_object.type == pg.MOUSEBUTTONDOWN:
            self.click = True
            self.update(event_object)

    def master(self):
        player_boxes = boxes_config = []
        conditonal = 0

        while conditonal < 2:

            self.screen.blit(self.fond, (0,0))

            for evenement in pg.event.get():
                if evenement.type == pg.QUIT: sys.exit()                    
                
                if evenement.type == pg.MOUSEBUTTONDOWN and self.button_coord.collidepoint(evenement.pos):
                    if conditonal > 2 :
                        self.click = True
                        self.update(evenement)
                    conditonal += 1

                # welcome page
                elif conditonal == 0:

                    self.message("grande", "WELCOME TO ABALONE", (30, 80, 100, 50), (255, 255, 255))
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
                    print("yeah")

                #     for k , i in zip(range(len(self.gamer_list)), range(0, 300, 60)):
                #         button = Jeu(pg.display.set_mode([800, 800]), (340 + i), 200, k, caption=self.gamer_list[k])
                #         self.message("petite", self.gamer_list[k], (341 + i, 220, 100, 50), "black")
                #         player_boxes.append(button)                        
                        
                #     for k, (i, j) in zip(range(len(self.configuration_list)),  zip(range(0, 600, 300), range(0, 300, 50))):
                #         button_config = Jeu(pg.display.set_mode([800, 800]), (200 + i), (363 + j), k, caption=self.configuration_list[k])
                #         self.message("petite", self.configuration_list[k], (220 + i, 360 + j, 100, 50), "black")
                #         boxes_config.append(button_config)
                            
                #     for box in player_boxes:
                #         box.update_box(evenement)
                #         if box.check:
                #             for b, b2 in zip(player_boxes,  boxes_config):
                #                 b2.update_box(evenement)
                #                 b.check = b == box
                #                 if b2.check:
                #                     for b in boxes_config:
                #                         b.check = b == box
                                                                
                #         for b1, b2 in zip(player_boxes, boxes_config):
                #             b1.render_box()
                #             b2.render_box()

                #         pg.display.flip()

                # self.screen.blit(self.fond, (0, 0))
                # pg.draw.rect(self.screen, (157, 99, 61, 255), (15, 120, 768, 550))
                # self.message("moyenne", "Configuration", (160, 50, 100, 50), (255, 255, 255))
                # self.message("petite", "Number of players", (350, 140, 100, 50), "black")
                # self.message("petite", "configuration table", (350, 300, 100, 50), "black")
                # self.screen.blit(self.play, self.play_coord)
                # self.screen.blit(self.parametre, (550, 30, 100, 50))
                
    def message(self, police, message, message_rectangle, couleur):
        if police == "petite":
            police = pg.font.SysFont('Times New Roman', 20, False)
        elif police == "moyenne":
            police = pg.font.SysFont('castellar', 40, False)
        elif police == "grande":
            police = pg.font.SysFont('castellar', 50, True)
        message = police.render(message, True, couleur)
        self.screen.blit(message, message_rectangle)