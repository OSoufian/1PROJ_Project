import pygame as pg


class PlayerInterface():

    def run(self, screen, players):
        font = pg.font.SysFont(None, 40)
        render = font.render("Validate", True, "black")
        message = font.render("écrivez votre nom", True, "black")
        message_rect = message.get_rect(x=screen.get_width()//2 - message.get_width()//2, y=message.get_height())
        message2 = font.render("appuyez pour valider le nom", True, "black")
        message_rect2 = message2.get_rect(x=screen.get_width()//2  - message2.get_width()//2, y=message_rect.y * 2)
        for number, player in enumerate(players):
            name = ""
            active_name = False
            validate = True
            input_name = pg.Rect(100, 100, 140, 40)
            input_color = pg.Rect(100, 200, 140, 32)
            validate_input = pg.Rect(500, 100, 140, 40)

            while validate:
                screen.fill((180, 50, 0))
                for event in pg.event.get():

                    if event.type == pg.MOUSEBUTTONDOWN:
                        active_name = input_name.collidepoint(event.pos)
                        validate = not validate_input.collidepoint(event.pos)


                    if event.type == pg.KEYDOWN:
            
                        if event.key == pg.K_BACKSPACE:
                            name = name[:-1]
                        elif event.key == pg.K_RETURN:
                            validate = False
                        else:   
                            if len(name) < 10:                           
                                name += event.unicode

                    if event.type == pg.QUIT:
                        pg.quit()

                pg.draw.rect(screen, "#333555", validate_input, border_radius=10)
                pg.draw.rect(screen, "brown", input_name, border_radius=10)
                txt_name = font.render(name, True, "black")
                screen.blit(render, (validate_input.x + 10, validate_input.y + 6))
                screen.blit(txt_name, (input_name.x, input_name.y + 5))
                pg.draw.rect(screen, "#666444", message_rect, border_radius=10)
                screen.blit(message, message_rect)
                pg.draw.rect(screen, "#666444", message_rect2, border_radius=10)
                screen.blit(message2, message_rect2)
                pg.display.flip()
                Nwidth = max(txt_name.get_width(), 20)
                input_name.w = Nwidth
            if len(players) == 2:
                player.name_rect = pg.Rect((200 + 200 * number * 1.5, 50), (Nwidth, 40))
            else:
                player.name_rect = pg.Rect((80 if number < 3 else 600, (20 + (number%3) * 60)), (Nwidth, 40))
            player.name_render = txt_name
            player.name = name
            name = ""
            screen.fill((180, 50, 0))
        for player in players:
            pg.draw.rect(screen, "brown", player.name_rect, border_radius=10)
            screen.blit(player.name_render, (player.name_rect.x, player.name_rect.y + 6))
            pg.draw.circle(screen, player.color, (player.name_rect.x - 30, player.name_rect.y + 18), 24)


