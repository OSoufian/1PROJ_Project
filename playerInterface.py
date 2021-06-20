import pygame as pg


class PlayerInterface():

    def run(self, screen, nb_joueur):
        players = []
        for player in range(nb_joueur):
            name= color = "" 
            active_name = active_color = False 
            validate = True
            font = pg.font.Font(None, 32)
            input_name = pg.Rect(100, 100, 140, 32) 
            input_color = pg.Rect(100, 200, 140, 32)
            validate_input = pg.Rect(1000, 300, 140, 32)

            while validate:
                for event in pg.event.get():

                    if event.type == pg.MOUSEBUTTONDOWN:
                        active_name = input_name.collidepoint(event.pos)
                        active_color = input_color.collidepoint(event.pos)
                        validate = validate_input.collidepoint(event.pos)
            
                    if event.type == pg.KEYDOWN:
            
                        if event.key == pg.K_BACKSPACE:
                            
                            if  active_name:
                                name = name[:-1]
                            else:
                                color = color[:-1]
                            
                        elif  active_name:
                            name += event.unicode
                                
                        else:                                
                            color += event.unicode

                txt_name = font.render(name, True, color)

                txt_color = font.render(color, True, color)

                Nwidth = max(30, txt_name.get_width()+10)
                input_name.w = Nwidth

                Cwidth = max(30, txt_color.get_width()+10)
                input_color.w = Cwidth
                
                pg.screen.blit()