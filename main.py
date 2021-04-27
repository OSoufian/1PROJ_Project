import pygame
from Abalone import CreateBoard
from Players import Player

pygame.init()
size = [800, 800]
screen = pygame.display.set_mode(size)

screen.fill((150, 255, 10))

pygame.display.flip()

running = True

pieces = {"p1": [], "p2": []}

board = CreateBoard([e // 2 for e in size], 250)
board.draw_regular_polygon(screen, (255, 255, 255), outline=10)
coordinates = board.draw_ceil(screen, (0, 0, 0), 2)

sprites = [pygame.draw.circle(screen, "green", i, coordinates[-1], 2) for i in coordinates[:-1]]

p1 = Player()
p1.circles = []
p2 = Player()
p2.circles = []
players = [p1, p2]


while running:

    for player in players:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in sprites if s.collidepoint(pos)]

                if len(clicked_sprites) >= 1:
                    coordinate_Circle = clicked_sprites[0].center

                    valid = False
                    #print([p.circles for p in players if coordinate_Circle in p.circles], coordinate_Circle)
                    if not any(p.circles for p in players if coordinate_Circle in p.circles):

                        player.circles.append(coordinate_Circle)
                        print(player.circles)
                        valid = True

                    print(player.name, "as clicked on ", coordinate_Circle, "and take for him"*valid)


    play = ""

    pygame.display.flip()

pygame.quit()
