import pygame as pg
from Abalone import CreateBoard
from Players import Player
from Marble import Marble
from interface import Jeu
from  saveBoard import readBoard, saveBoard
from vector import Vector2

pg.init()
size = [800, 800]
screen = pg.display.set_mode(size)

Begin = Jeu(screen)
Begin.master()

mod, nb_player = Begin.mod_player

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

players = [Player("white", "Toto"),  Player("black", "Hercule")]

for player, circle in zip(players, readBoard(nb_player, mod)):
    player.marbles = [*map(tuple, circle)]

list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
list_x = [list(range(0, 5)), list(range(0, 6)), list(range(0, 7)), list(range(0, 8)), list(range(0, 9)),
            list(range(0, 8)), list(range(0, 7)), list(range(0, 6)), list(range(0, 5))]
middle = coordinates[len(list_coo_x)//2]

indice_x = coordinates.index(middle)
indice_y = middle.index(middle[len(middle)//2])
x, y = middle[len(middle)//2]

lenX = len(list_coo_x)
lenCo = len(coordinates)
where = lenX//2
Marble = Marble(screen, coordinates, players)

# Prends en paramètres des index dans le board et retourne des coordonnées
def get_coordinates(x, y):
    return coordinates[y][x]

# Prends en paramètres des coordonnées et retourne les index dans le tableau
def get_index(xy):
    for row in range(9):
        for column in list_x[row]:
            if coordinates[row][column] == xy:
                return row, column

def create_table():
    play = 0
    if event.type == pg.MOUSEBUTTONDOWN:
            clicked_sprites = [s for
                               s in sprites
                               if s.collidepoint(pg.mouse.get_pos())]

            coordinate_circle = clicked_sprites[0].center

            player = players[play % len(players)]

            while (len(clicked_sprites) >= 1 and
                    len(players[play % len(players)].circles) < 14 and
                    not any(p.circles for
                            p in players if coordinate_circle in p.circles)):

                player.circles.append(coordinate_circle)
                pg.draw.circle(screen,
                                   player.color,
                                   coordinate_circle,
                                   radius-3)

                play += 1

coordinate = [coordinates[i][j] for i in range(len(coordinates)) for j in range(len(coordinates[i]))]
bool = False
turn = 0

while running:
    current_player = players[turn%len(players)]
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        for circle in Marble.neighbor((x, y)):
            pg.draw.circle(screen, (250, 159, 122), circle, radius)
            pg.draw.circle(screen, (180, 50, 0), circle, radius, 3)

        pg.draw.circle(screen, (255, 255, 255), (x, y), radius, 2)
        for i in players:
            for j in i.marbles:
                pg.draw.circle(screen, i.color, j, radius - 3)

        if event.type == pg.KEYDOWN:
            key = pg.key.get_pressed()

            if key[pg.K_LEFT]:
                if indice_x == 0:
                    pass
                else:
                    indice_x -= 1

            if key[pg.K_RIGHT]:
                if indice_x == len(coordinates[indice_y])-1:
                    pass
                else:
                    indice_x += 1

            if key[pg.K_UP]:
                if indice_y == 0:
                    pass
                elif indice_y <= 4 and indice_x == len(coordinates[indice_y])-1:
                    indice_y -= 1
                    indice_x -= 1
                else:
                    indice_y -= 1

            if key[pg.K_DOWN]:
                if indice_y == 8:
                    pass
                elif indice_y >= 4 and indice_x == len(coordinates[indice_y]) - 1:
                    indice_y += 1
                    indice_x -= 1
                else:
                    indice_y += 1

            x, y = get_coordinates(indice_x, indice_y)
            if (key[pg.K_SPACE] and (x, y) not in Marble.selected and len(Marble.selected) < 3
            and ((x, y) in current_player.marbles)):
                if not Marble.selected:
                    Marble.selected.append((x, y))

                elif len(Marble.selected) == 1 and Marble.selected[0] in Marble.neighbor((x, y)):
                    Marble.selected.append((x, y))

                elif len(Marble.selected) == 2:
                    row, column = get_index((x, y))
                    row1, column1 = get_index(Marble.selected[0])
                    row2, column2 = get_index(Marble.selected[1])
                    row3 = row1 - row2
                    column3 = column1 - column2

                    if ((row == row1 + row3 and column == column1 + column3) or
                    (row == row1 - row3 and column == column1 - column3) or
                    (row == row2 + row3 and column == column2 + column3) or
                    (row == row2 - row3 and column == column2 - column3)):
                        Marble.selected.append((x, y))

            elif key[pg.K_SPACE] and (x, y) in Marble.selected:
                if not (len(Marble.selected) == 3 and Marble.selected[-1] != Marble.selected[1] and (x, y) == Marble.selected[1]):
                    Marble.selected.remove((x, y))
                continue

            if key[pg.K_a] and (x, y) not in Marble.selected:
                if len(Marble.selected) == 1:
                    if Marble.move(current_player, Marble.selected[-1], (x, y)):
                        turn += 1
                    pg.draw.circle(screen, (180, 50, 0), Marble.selected[-1], radius, 3)
                    Marble.selected = []


        for circle in [i for i in coordinate if i not in [(c, d) for player in players for c, d in player.marbles]]:
                pg.draw.circle(screen, (250, 159, 122), circle, radius-5)

        for circle in Marble.selected:
            pg.draw.circle(screen, (255, 0, 255), circle, radius, 2)

        if Marble.selected:
            if len(Marble.selected) == 1:
                for circle in Marble.possibility(Marble.selected[-1]):
                    pg.draw.circle(screen, (158, 240, 78), circle, radius - 10)

            elif len(Marble.selected) == 2:
                choice1, choice2 = Marble.selected
                choice1_index = get_index(choice1)
                choice2_index = get_index(choice2)
                vector = Vector2((choice2_index[0] - choice1_index[0], choice2_index[1] - choice1_index[1]))
                mixx = Marble.neighbor(choice1) + Marble.neighbor(choice2)
                mix = []
                for i in mixx:
                    if not mixx.count(i) > 1:
                        mix.append(i)
                # mix = [i for i in mix if not mix.count(i) > 1]
                a = [get_index(i) for i in mix]
                for xx, yy in a:
                    if xx >= 0 and yy >= 0 and coordinates[xx][yy] not in current_player.marbles:
                        v = vector.convert(xx, yy)
                        if coordinates[v.x][v.y] not in current_player.marbles or coordinates[v.x][v.y] in Marble.selected:
                            pg.draw.circle(screen, (158, 240, 78), coordinates[xx][yy], radius - 10)

    pg.display.flip()

pg.quit()
