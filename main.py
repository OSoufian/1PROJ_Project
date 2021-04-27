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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    board = CreateBoard([e // 2 for e in size], 250)
    board.draw_regular_polygon(screen, (255, 255, 255), outline=10)
    coordinates = board.draw_ceil(screen, (0, 0, 0), 2)

    for i in coordinates[:-1]:
        pygame.draw.circle(screen, "black", i, coordinates[-1], 2)

    play = ""

    pygame.display.flip()

pygame.quit()
