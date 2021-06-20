import pygame as pg
from pygame.draw import circle
from vector import Vector2


class Marble:
    def __init__(self, surface, coordinates, players):
        self.coordinates = coordinates
        self.surface = surface
        self.players = players
        self.selected = []

    def draw_clickable(self, coordinate_ceil, color=(255, 255, 255)):
        assert coordinate_ceil in self.coordinates, "Coordiante outside shape"
        pg.draw.circle(self.surface, color, coordinate_ceil, coordinate_ceil[-1])

    def neighbor(self, xy):
        var = [e for e in self.coordinates if xy in e][0]
        indice_y = self.coordinates.index(var)
        indice_x = var.index(xy)
        neighbor = []

        if indice_y - 1 < len(self.coordinates) and 0 <= indice_y - 1:
            if indice_x < len(self.coordinates[indice_y - 1]) and 0 <= indice_x:

                neighbor.append(self.coordinates[indice_y - 1][indice_x])
                if indice_x == 0 and indice_y > 4:
                    neighbor.append(self.coordinates[indice_y - 1][indice_x + 1])

            if indice_x - 1 < len(self.coordinates[indice_y - 1]) and 0 <= indice_x - 1:
                neighbor.append(
                    self.coordinates[indice_y - 1][
                        indice_x + 1 if indice_y > 4 else indice_x - 1
                    ]
                )

        if indice_y + 1 < len(self.coordinates) and -1 < indice_y + 1:
            if indice_x < len(self.coordinates[indice_y + 1]) and 0 <= indice_x:
                neighbor.append(self.coordinates[indice_y + 1][indice_x])

                if indice_x == 0 and indice_y < 4:
                    neighbor.append(self.coordinates[indice_y + 1][indice_x + 1])

            if indice_x - 1 < len(self.coordinates[indice_y + 1]) and 0 <= indice_x - 1:
                neighbor.append(
                    self.coordinates[indice_y + 1][
                        indice_x + 1 if indice_y < 4 else indice_x - 1
                    ]
                )

        if indice_y < len(self.coordinates) and -1 < indice_y:
            if indice_x + 1 < len(self.coordinates[indice_y]) and 0 <= indice_x + 1:
                neighbor.append(self.coordinates[indice_y][indice_x + 1])
            if indice_x - 1 < len(self.coordinates[indice_y]) and -1 < indice_x - 1:
                neighbor.append(self.coordinates[indice_y][indice_x - 1])

        return neighbor

    def possibility(self, xy):
        coordinates = set(
            [(c, d) for player in self.players for c, d in player.marbles]
        )
        deffault = set((x, y) for x, y in self.neighbor(xy))
        return tuple(deffault.difference(coordinates))

    def move(
        self, player, old_coordinate, new_coordinate, len, funclen2=None, get_index=None
    ):
        if len == 1 and new_coordinate in self.possibility(old_coordinate):
            player.marbles.remove(old_coordinate)
            player.marbles.append(new_coordinate)
            return True
        if len in (2, 3) and new_coordinate in funclen2():
            for i in self.neighbor(new_coordinate):
                if i in self.selected:
                    break
            new_index = get_index(new_coordinate)
            old_index = get_index(i)
            v = Vector2((new_index[0] - old_index[0], new_index[1] - old_index[1]))
            for i in self.selected:
                xx, yy = get_index(i)
                vector_converted = v.convert(xx, yy)
                player.marbles.remove(i)
                if (
                    new_index[0] in (3, 5)
                    and (xx, yy) != old_index
                    and not all([get_index(i)[0] == 4 for i in self.selected])
                    and any([get_index(i)[0] == 4 for i in self.selected])
                ):
                    player.marbles.append(
                        self.coordinates[vector_converted.x][vector_converted.y + 1]
                    )
                else:
                    player.marbles.append(
                        self.coordinates[vector_converted.x][vector_converted.y]
                    )
                print(vector_converted)

            return True
        return False
