import pygame as pg
from Abalone import CreateBoard
from Players import Player
from Marble import Marble
from interface import Jeu
import time

pg.init()
size = [800, 800]
screen = pg.display.set_mode(size)

Begin = Jeu(screen)
Begin.master()

screen.fill((180, 50, 0))

background = pg.transform.scale(pg.image.load("./Menu/fond.jpg"), size)

pg.display.flip()

clock = pg.time.Clock()

clock.tick(10)

running = True

board = CreateBoard([e // 2 for e in size], 250)
board.draw_regular_polygon(screen, (250, 100, 50))
board.draw_regular_polygon(screen, (0, 0, 0), 5)
radius, sprites = board.draw_ceil(screen, (250, 159, 122), 2)
coordinates = board.coordinates

board1 = "Standard"

players = [Player("white", "Toto"),  Player("black", "Hercule")]

nPlayers = len(players)

turn = 0
current_player = players[turn%nPlayers]

if board1 == "Standard":

    circles = [(295.5258238486492, 216.52582384864922), (348.5774715459477, 216.52582384864922), (401.6291192432461, 216.52582384864922), \
        (454.6807669405446, 216.52582384864922), (507.732414637843, 216.52582384864922), (269.0, 262.5774715459477), \
            (322.05164769729845, 262.5774715459477), (375.1032953945969, 262.5774715459477), (428.15494309189535, 262.5774715459477), \
                (481.2065907891938, 262.5774715459477), (534.2582384864922, 262.5774715459477), (348.5774715459477, 308.6291192432461), \
                    (401.6291192432461, 308.6291192432461), (454.6807669405446, 308.6291192432461)],\
                    [
                        (348.5774715459477, 492.8357100324399), (401.6291192432461, 492.8357100324399), (454.6807669405446, 492.8357100324399), \
                        (269.0, 538.8873577297384), (322.05164769729845, 538.8873577297384), (375.1032953945969, 538.8873577297384), \
            (428.15494309189535, 538.8873577297384), (481.2065907891938, 538.8873577297384), (534.2582384864922, 538.8873577297384), \
                (295.5258238486492, 584.9390054270368), (348.5774715459477, 584.9390054270368), (401.6291192432461, 584.9390054270368), \
                    (454.6807669405446, 584.9390054270368), (507.732414637843, 584.9390054270368)]
    
    for player, circle in zip(players, circles):
        player.marbles = circle 

list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
list_x = [list(range(0, 5)), list(range(0, 6)), list(range(0, 7)), list(range(0, 8)), list(range(0, 9))\
        , list(range(0, 8)), list(range(0, 7)), list(range(0, 6)), list(range(0, 5))]
middle = coordinates[len(list_coo_x)//2]

indice_x = coordinates.index(middle)
indice_y = middle.index(middle[len(middle)//2])
x, y = middle[len(middle)//2]

lenX = len(list_coo_x)
lenCo = len(coordinates)
where = lenX//2

Marble.selected = []

# Prends en paramètres des index dans le board et retourne des coordonnées
def get_coordinates(x, y):
    return coordinates[y][x]


# Prends en paramètres des coordonnées et retourne les index dans le board
def get_index(xy):    
    for row in range(9):
        for column in list_x[row]:
            if coordinates[row][column] == xy:
                return row, column

get_index((348.5774715459477, 216.52582384864922))


def create_table():
    play = 0
    if event.type == pg.MOUSEBUTTONDOWN:
            clicked_sprites = [s for
                               s in sprites
                               if s.collidepoint(pg.mouse.get_pos())]

            coordinate_circle = clicked_sprites[0].center

            player = players[play % nPlayers]

            while len(clicked_sprites) >= 1 and\
                    len(players[play % nPlayers].circles) < 14 and \
                    not any(p.circles for
                            p in players if coordinate_circle in p.circles):

                player.circles.append(coordinate_circle)
                pg.draw.circle(screen,
                                   player.color,
                                   coordinate_circle,
                                   radius-3)

                play += 1

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        for player in players:
            for circle in player.marbles:
                pg.draw.circle(screen, player.color, circle, radius-3)

        # len([p for p in players if len(p.circles)==14]) == nPlayers
        if True:
            for circle in Marble(screen, coordinates, players).neighbor((x, y)):
                pg.draw.circle(screen, (180, 50, 0), circle, radius, 2)

            selector = pg.draw.circle(screen, (255, 255, 255), (x, y), radius, 2)

            if event.type == pg.KEYDOWN:
                key = pg.key.get_pressed()

                if key[pg.K_LEFT]:
                    if indice_x == 0:
                        continue
                    else:
                        indice_x -= 1

                if key[pg.K_RIGHT]:
                    if indice_x == len(coordinates[indice_y])-1:
                        continue
                    else:
                        indice_x += 1

                if key[pg.K_UP]:
                    if indice_y == 0:
                        continue
                    elif indice_y <= 4 and indice_x == len(coordinates[indice_y])-1:
                        indice_y -= 1
                        indice_x -= 1
                    else:
                        indice_y -= 1

                if key[pg.K_DOWN]:
                    if indice_y == 8:
                        continue
                    elif indice_y >= 4 and indice_x == len(coordinates[indice_y]) - 1:
                        indice_y += 1
                        indice_x -= 1
                    else:
                        indice_y += 1

                pg.draw.circle(screen, (180, 50, 0), (int(x), int(y)), radius, 2)
                x, y = get_coordinates(indice_x, indice_y)

                if key[pg.K_SPACE] and (x, y) not in Marble.selected and len(Marble.selected) < 3 \
                and ((x, y) in current_player.marbles):
                    if Marble.selected == []:
                        Marble.selected.append((x, y))
                        print(Marble.selected)
                        old_x, old_y = indice_x, indice_y
                        
                    elif len(Marble.selected) == 1 and Marble.selected[0] in Marble(screen, coordinates, players).neighbor((x, y)):
                        Marble.selected.append((x, y))

                    elif len(Marble.selected) == 2:
                        row, column = get_index((x, y))
                        row1, column1 = get_index(Marble.selected[0])
                        row2, column2 = get_index(Marble.selected[1])
                        row3 = row1 - row2
                        column3 = column1 - column2

                        if (row == row1 + row3 and column == column1 + column3) or \
                        (row == row1 - row3 and column == column1 - column3) or \
                        (row == row2 + row3 and column == column2 + column3) or \
                        (row == row2 - row3 and column == column2 - column3):
                           Marble.selected.append((x, y))              


                elif key[pg.K_SPACE] and (x, y) in Marble.selected:
                    Marble.selected.remove((x, y))   


            # if key[pg.K_RETURN] and len(Marble.selected) == 1:
            #     while True :
            #         if key[pg.K_SPACE] and (x, y) in Marble(screen, coordinates, players).neighbor(Marble.selected[0]) and ((x, y) not in current_player.marbles):
            #             for coordinates in current_player.marbles:
            #                 if coordinates == Marble.selected[0]:
            #                     current_player.marbles.pop(coordinates)
            #                     current_player.marbles.append((x, y))
            #                     break 
                          
            for circle in Marble(screen, coordinates, players).neighbor((x, y)):
                pg.draw.circle(screen, (255, 255, 255), circle, radius, 2)

            for circle in Marble.selected:
                pg.draw.circle(screen, (255, 0, 255), circle, radius, 2)

    pg.display.flip()

pg.quit()
