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

    def can_move(self, coordinate, current_player):
        selected = sorted(self.selected)
        abs1, abs2, *abs3 = selected
        vector = Vector2((abs1[0] - abs2[0], abs1[1] - abs2[1]))
        converted = vector.convert(*abs1).indice
        if converted in coordinate and converted not in current_player.marbles:
            yield converted
        vector = -vector
        converted = vector.convert(*selected[-1]).indice
        if converted in coordinate and converted not in current_player.marbles:
            yield converted
        mixx = self.neighbor(abs1) + self.neighbor(abs2) + (self.neighbor(*abs3) if abs3 else [])
        mix = [i for i in mixx if mixx.count(i) <= 1 and i not in [(c, d) for player in self.players for c, d in player.marbles]]
        for i in mix:
            nearest_value, *_ = [i for i in self.neighbor(i) if i in selected]
            vector_2 = Vector2((i[0] - nearest_value[0], i[1] - nearest_value[1]))
            for j in selected:
                coordina = vector_2.convert(*j)
                if coordina.indice in [(c, d) for player in self.players for c, d in player.marbles]:
                    break
            else:
                yield i

    def move(
        self, player, old_coordinate, new_coordinate, len, args:tuple=None, get_index=None
    ):
        if len == 1 and new_coordinate in self.possibility(old_coordinate):
            player.marbles.remove(old_coordinate)
            player.marbles.append(new_coordinate)
            return True
        if len in (2, 3) and new_coordinate in self.can_move(*args):
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

            return True
        return False
