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
    p1.marbles = (295, 216), (348, 216), (401, 216), (454, 216), (507,216),\
                  (269, 262), (322, 262), (375, 262), (428, 262), (481, 262), (534, 262),\
                  (348, 308), (401, 308), (454, 308)

    p2.marbles = (348, 492), (401, 492), (454, 492),\
                  (269, 538), (322, 538), (375, 538), (428, 538), (481, 538), (534, 538),\
                  (295, 584), (348, 584), (401, 584), (454, 584), (507,584)


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

# def create_table():
#     if event.type == pygame.MOUSEBUTTONDOWN:
#             clicked_sprites = [s for
#                                s in sprites
#                                if s.collidepoint(pygame.mouse.get_pos())]

#             coordinate_circle = clicked_sprites[0].center

#             player = players[play % nPlayers]

#             while len(clicked_sprites) >= 1 and\
#                     len(players[play % nPlayers].circles) < 14 and \
#                     not any(p.circles for
#                             p in players if coordinate_circle in p.circles):

#                 player.circles.append(coordinate_circle)
#                 pygame.draw.circle(screen,
#                                    player.color,
#                                    coordinate_circle,
#                                    radius-3)

#                 play += 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # for circle in p1.get_marbles():
        #     for coordinates in circle.get_coordinates():
        #         pygame.draw.circle(screen, p1.get_color(), circle, radius-3)

        # for circle in p2.get_marbles():
        #     for coordinates in circle.get_coordinates():
        #         pygame.draw.circle(screen, p2.get_color(), circle, radius-3)

        for circle in p1.marbles[0]:
            pygame.draw.circle(screen, p1.color, circle, radius-3)

        for circle in p2.marbles[0]:
            pygame.draw.circle(screen, p2.color, circle, radius-3)

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

                # if key[pygame.K_SPACE] and \
                # (x, y) not in selected_circle and \
                # len(selected_circle) < 3 \
                # and ((int(x),int(y)) in p1.get_marbles() or (int(x),int(y)) in p2.get_marbles()):
                #     if len(selected_circle) == 0:
                #         selected_circle.append((int(x), int(y)))
                #     elif len(selected_circle) > 0 and (int(x),int(y)) in p1.get_marbles() and p2.get_marbles() not in selected_circle:
                #         selected_circle.append((int(x), int(y)))

                if key[pygame.K_SPACE] and \
                (x, y) not in selected_circle and \
                len(selected_circle) < 3 \
                and ((int(x),int(y)) in p1.marbles[0] \
                or (int(x),int(y)) in p2.marbles[0]):
                    selected_circle.append((x, y))
                    # if len(selected_circle) == 0:
                    #     selected_circle.append((x, y))
                    # elif len(selected_circle) > 0 and p1.marbles[0] in selected_circle and (int(x),int(y)) in p1.marbles[0]:
                    #     selected_circle.append((x, y))
                    # elif len(selected_circle) > 0 and p2.marbles[0] in selected_circle and (int(x),int(y)) in p2.marbles[0]:
                    #     selected_circle.append((x, y))

                
                    

                elif key[pygame.K_SPACE] and \
                (x, y) in selected_circle:
                    selected_circle.remove((x, y))          

    
                          


            for circle in\
                    Marble(screen, coordinates, players).neighbor((x, y)):
                pygame.draw.circle(screen, (255, 255, 255), circle, radius, 2)

            for circle in selected_circle:
                pygame.draw.circle(screen, (255, 0, 255), circle, radius, 2)

    pygame.display.flip()


pygame.quit()

