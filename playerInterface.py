import pygame as pg


class PlayerInterface():

    def run(self, screen, players):
        for player in players:
            name = ""
            active_name = active_color = False 
            validate = True
            font = pg.font.SysFont("arial", 32)
            input_name = pg.Rect(100, 100, 140, 40)
            input_color = pg.Rect(100, 200, 140, 32)
            validate_input = pg.Rect(100, 300, 140, 32)

            while validate:
                for event in pg.event.get():

                    if event.type == pg.MOUSEBUTTONDOWN:
                        active_name = input_name.collidepoint(event.pos)
                        validate = validate_input.collidepoint(event.pos)

                    if event.type == pg.KEYDOWN:
            
                        if event.key == pg.K_BACKSPACE:
                            name = name[:-1]
                        else:                                
                            name += event.unicode

                    if event.type == pg.QUIT:
                        pg.quit()

                pg.draw.rect(screen, "#555555", input_name, border_radius=10)
                txt_name = font.render(name, False, "black")
                screen.blit(txt_name, input_name)
                print(name)
                pg.display.flip()


                Nwidth = txt_name.get_width()
                input_name.w = Nwidth
            
            player.name = name
