from typing import Match
import pygame as pg
from Abalone import CreateBoard
from Players import Player
from Marble import Marble
from interface import Jeu
from  saveBoard import readBoard, saveBoard

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
# players = [Player("white", "Soufian"),  Player("black", "Lounes"), Player("grey", "Akito")] #test 3 joueurs
# players = [Player("cyan2", "Soufian"),  Player("chartreuse4", "Lounes"), Player("darkolivegreen3", "Akito"), Player("blue4", "Marceljordan")] #test 4 joueurs
# players = [Player("red3", "Soufian"),  Player("gold", "Lounes"), Player("darkorchid", "Akito"), Player("chartreuse3", "Marceljordan"), Player("blue4", "Lucas")] #test 5 joueurs
# players = [Player("cyan2", "Soufian"),  Player("springgreen4", "Lounes"), Player("orchid2", "Akito"), Player("dodgerblue4", "Marceljordan"), Player("darkolivegreen2", "Lucas"), Player("darkorchid3", "Cyprien")] #test 6 joueurs

turn = 0
current_player = players[turn%len(players)]
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


# Prends en paramètres des coordonnées et retourne les index dans le board
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
# print(coordinate)
liste = [i for i in coordinate if i not in [(c, d) for player in players for c, d in player.marbles]]
# print(len(liste))
bool = False
select_next = 0
bool2 = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if select_next ==0:

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

            pg.draw.circle(screen, (180, 50, 0), (int(x), int(y)), radius, 3)
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
                Marble.selected.remove((x, y))
                
            if key[pg.K_RETURN] and bool:
                player.marbles.remove(Marble.selected[-1] if Marble.selected[-1] in player.marbles else Marble.selected[0])
                player.marbles.append((x, y))
                print(key[pg.K_SPACE] and all((x, y) in Marble.possibility(caca := Marble.selected[i]) for i in range(len(caca))))
            
            if key[pg.K_RETURN] and len(Marble.selected) >= 1:
                bool = not bool
                

            if key[pg.K_SPACE] and (x, y) in Marble.possibility(Marble.selected[-1]):
                print("lol")
                bool2 = not bool2

        # for circle in liste:
        #     pg.draw.circle(screen, (250, 159, 122), circle, radius-5)

                        
        for circle in Marble.neighbor((x, y)):
            pg.draw.circle(screen, (255, 255, 255), circle, radius, 2)

        for circle in Marble.selected:
            pg.draw.circle(screen, (255, 0, 255), circle, radius, 2)

        if bool:
            for circle in Marble.possibility(Marble.selected[-1]) + Marble.possibility(Marble.selected[0]):
                    pg.draw.circle(screen, (158, 240, 78), circle, radius - 10)

        # if bool2 and bool:# and all(circle in Marble.possibility(Marble.selected[i]) for i in range(len(Marble.selected)))
        #     print(Marble.selected)
        #     player.marbles.remove(Marble.selected[-1] if Marble.selected[-1] in player.marbles else Marble.selected[0])
        #     player.marbles.append((x, y))
        #     print(Marble.selected)
        #     # Marble.selected, (x, y)

    pg.display.flip()

pg.quit()