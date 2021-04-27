import pygame
from Abalone import CreateBoard

pygame.init()
size = [800, 800]
screen = pygame.display.set_mode(size)

screen.fill((150, 255, 10))

pygame.display.flip()

running = True

pieces = {"p1": [], "p2": []}

while running:

    board = CreateBoard([e // 2 for e in size], 250)
    board.draw_regular_polygon(screen, (255, 255, 255), outline=10)
    coordinates = board.draw_ceil(screen, (0, 0, 0), 2)

    sprites = [pygame.draw.circle(screen, "black", i, coordinates[-1], 2) for i in coordinates[:-1]]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in sprites if s.collidepoint(pos)]

            if len(clicked_sprites) >= 1:
                print(clicked_sprites[0].center)


    play = ""

    pygame.display.flip()

pygame.quit()
