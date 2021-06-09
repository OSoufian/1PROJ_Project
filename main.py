import pygame
from Abalone import CreateBoard
from Players import Player
from Marble import Marble
from interface import Jeu
import time

pygame.init()
size = [800, 800]
screen = pygame.display.set_mode(size)

Jeu(screen).master()
pygame.display.flip()

screen.fill((180, 50, 0))
background = pygame.transform.scale(pygame.image.load("./Menu/fond.jpg"), size)

pygame.display.flip()

clock = pygame.time.Clock()

clock.tick(10)

running = True

board = CreateBoard([e // 2 for e in size], 250)
board.draw_regular_polygon(screen, (250, 100, 50))
board.draw_regular_polygon(screen, (0, 0, 0), 5)
radius, sprites = board.draw_ceil(screen, (250, 159, 122), 2)
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
nPlayers = len(players)

play = 0

list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
middle = coordinates[len(list_coo_x)//2]

indice_x = coordinates.index(middle)
indice_y = middle.index(middle[len(middle)//2])
x, y = middle[len(middle)//2]

lenX = len(list_coo_x)
lenCo = len(coordinates)
where = lenX//2

selected_circle = []


def get_coordinates(x, y):
    return coordinates[y][x]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_sprites = [s for
                               s in sprites
                               if s.collidepoint(pygame.mouse.get_pos())]

            coordinate_circle = clicked_sprites[0].center

            player = players[play % nPlayers]

            while len(clicked_sprites) >= 1 and\
                    len(players[play % nPlayers].circles) < 14 and \
                    not any(p.circles for
                            p in players if coordinate_circle in p.circles):

                player.circles.append(coordinate_circle)
                pygame.draw.circle(screen,
                                   player.color,
                                   coordinate_circle,
                                   radius-3)

                play += 1
        # len([p for p in players if len(p.circles)==14]) == nPlayers
        if True:
            for circle in \
                    Marble(screen, coordinates, players).neighbor((x, y)):
                pygame.draw.circle(screen, (180, 50, 0), circle, radius, 2)

            selector = \
                pygame.draw.circle(screen, (255, 255, 255), (x, y), radius, 2)

            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()

                if key[pygame.K_LEFT]:
                    if indice_x == 0:
                        continue
                    else:
                        indice_x -= 1

                if key[pygame.K_RIGHT]:
                    if indice_x == len(coordinates[indice_y])-1:
                        continue
                    else:
                        indice_x += 1

                if key[pygame.K_UP]:
                    if indice_y == 0:
                        continue
                    elif indice_y <= 4 and \
                            indice_x == len(coordinates[indice_y])-1:
                        indice_y -= 1
                        indice_x -= 1
                    else:
                        indice_y -= 1

                if key[pygame.K_DOWN]:
                    if indice_y == 8:
                        continue
                    elif indice_y >= 4 and \
                            indice_x == len(coordinates[indice_y])-1:
                        indice_y += 1
                        indice_x -= 1
                    else:
                        indice_y += 1

                pygame.draw.circle(screen, (180, 50, 0), (x, y), radius, 2)
                x, y = get_coordinates(indice_x, indice_y)
                pygame.display.update()

                if key[pygame.K_SPACE] and \
                        (x, y) not in selected_circle and \
                        len(selected_circle) <= 3:
                    selected_circle.append((x, y))

            for circle in\
                    Marble(screen, coordinates, players).neighbor((x, y)):
                pygame.draw.circle(screen, (255, 255, 255), circle, radius, 2)

            for circle in selected_circle:
                pygame.draw.circle(screen, (255, 0, 255), circle, radius, 2)

    pygame.display.flip()


pygame.quit()
