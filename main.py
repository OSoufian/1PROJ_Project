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
radius, sprites = board.draw_ceil(screen, (0, 0, 0), 2)
coordinates = board.coordinates

p1 = Player()
p1.circles = []
p1.name = "Toto"
p1.color = "white"

p2 = Player()
p2.circles = []
p2.name = "Hercule"
p2.color = "black"

players = [p1, p2]

play = 0

game_init = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in sprites if s.collidepoint(pos)]

            if len(clicked_sprites) >= 1:
                if [p for p in players if len(p.circles) == 14]:
                    game_init = False
                coordinate_Circle = clicked_sprites[0].center

                valid = False
                # print([p.circles for p in players if coordinate_Circle in p.circles], coordinate_Circle)
                if not any(p.circles for p in players if coordinate_Circle in p.circles) and game_init:
                    players[play % 2].circles.append(coordinate_Circle)
                    pygame.draw.circle(screen, players[play%2].color, coordinate_Circle, radius)
                    print(players[play % 2].circles)
                    valid = True
                print(players[play % 2].name, "as clicked on ", coordinate_Circle, "and take for him" * valid)
                play += 1

        if event.type == pygame.KEYDOWN:
            running = False


    pygame.display.flip()

pygame.quit()
