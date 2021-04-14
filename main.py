import pygame
from Abalone import CreateBoard

pygame.init()
size = [1000, 1000]
screen = pygame.display.set_mode(size)

screen.fill((150, 255, 10))

pygame.display.flip()

running = True

pieces = {"p1": [], "p2": []}

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board = CreateBoard([e // 2 for e in size], 360)
    board.draw_regular_polygon(screen, (255, 255, 255), outline=10)
    coordinate = board.get_coordinates()
    play = ""

    pygame.display.flip()

pygame.quit()
