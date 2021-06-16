import pygame
from Abalone import CreateBoard
from Players import Player
from Marble import Marble
from interface import Jeu
import time

pygame.init()
size = [800, 800]
screen = pygame.display.set_mode(size)

Begin = Jeu(screen, 200, 200, 1)
Begin.master()

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

board = "Standard"

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

turn = 0
current_player = players[turn%nPlayers]

if board == "Standard":
    p1.marbles = (295.5258238486492, 216.52582384864922), (348.5774715459477, 216.52582384864922), (401.6291192432461, 216.52582384864922), \
        (454.6807669405446, 216.52582384864922), (507.732414637843, 216.52582384864922), (269.0, 262.5774715459477), \
            (322.05164769729845, 262.5774715459477), (375.1032953945969, 262.5774715459477), (428.15494309189535, 262.5774715459477), \
                (481.2065907891938, 262.5774715459477), (534.2582384864922, 262.5774715459477), (348.5774715459477, 308.6291192432461), \
                    (401.6291192432461, 308.6291192432461), (454.6807669405446, 308.6291192432461)

    p2.marbles = (348.5774715459477, 492.8357100324399), (401.6291192432461, 492.8357100324399), (454.6807669405446, 492.8357100324399), \
        (269.0, 538.8873577297384), (322.05164769729845, 538.8873577297384), (375.1032953945969, 538.8873577297384), \
            (428.15494309189535, 538.8873577297384), (481.2065907891938, 538.8873577297384), (534.2582384864922, 538.8873577297384), \
                (295.5258238486492, 584.9390054270368), (348.5774715459477, 584.9390054270368), (401.6291192432461, 584.9390054270368), \
                    (454.6807669405446, 584.9390054270368), (507.732414637843, 584.9390054270368)



list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
middle = coordinates[len(list_coo_x)//2]

indice_x = coordinates.index(middle)
indice_y = middle.index(middle[len(middle)//2])
x, y = middle[len(middle)//2]

lenX = len(list_coo_x)
lenCo = len(coordinates)
where = lenX//2

Marble.selected = []

def get_coordinates(x, y):
    return coordinates[y][x]

def create_table():
    play = 0
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for circle in p1.marbles[0]:
            pygame.draw.circle(screen, p1.color, circle, radius-3)

        for circle in p2.marbles[0]:
            pygame.draw.circle(screen, p2.color, circle, radius-3)

        # len([p for p in players if len(p.circles)==14]) == nPlayers
        if True:
            for circle in Marble(screen, coordinates, players).neighbor((x, y)):
                pygame.draw.circle(screen, (180, 50, 0), circle, radius, 2)

            selector = pygame.draw.circle(screen, (255, 255, 255), (x, y), radius, 2)

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
                    elif indice_y <= 4 and indice_x == len(coordinates[indice_y])-1:
                        indice_y -= 1
                        indice_x -= 1
                    else:
                        indice_y -= 1

                if key[pygame.K_DOWN]:
                    if indice_y == 8:
                        continue
                    elif indice_y >= 4 and indice_x == len(coordinates[indice_y])-1:
                        indice_y += 1
                        indice_x -= 1
                    else:
                        indice_y += 1


                pygame.draw.circle(screen, (180, 50, 0), (int(x), int(y)), radius, 2)
                x, y = get_coordinates(indice_x, indice_y)
                pygame.display.update()                

                if key[pygame.K_SPACE] and (x, y) not in Marble.selected and len(Marble.selected) < 3 \
                and ((x, y) in current_player.marbles[0]):
                    if Marble.selected == []:
                        Marble.selected.append((x, y))
                        print(Marble.selected)
                    elif len(Marble.selected) == 1 and Marble.selected[0] in Marble(screen, coordinates, players).neighbor((x, y)):
                        Marble.selected.append((x, y))
                        print(Marble.selected)
                    # else:
                    #     for sub in coordinates:
                    #        if all(l for l in player.marbles if l in sub) :

                    """
                    Pour flat une list

                    ma liste à flat est test

                    test =[l for sub in]
                    """


                elif key[pygame.K_SPACE] and (x, y) in Marble.selected:
                    Marble.selected.remove((x, y))    
                          


            for circle in Marble(screen, coordinates, players).neighbor((x, y)):
                pygame.draw.circle(screen, (255, 255, 255), circle, radius, 2)

            for circle in Marble.selected:
                pygame.draw.circle(screen, (255, 0, 255), circle, radius, 2)

    pygame.display.flip()

pygame.quit()

