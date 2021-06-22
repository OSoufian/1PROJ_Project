import pygame as pg
from pygame.draw import circle
from vector import Vector2


class Marble:
    def __init__(self, surface, coordinates, players):
        self.coordinates = coordinates
        self.surface = surface
        self.players = players
        self.selected = []
        self.to_move = []


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
        for coef, value in zip(range(-1, 2, 2), (selected[-1], abs1)):
            _vector = vector * coef
            converted = _vector.convert(*value).indice
            index = 1
            if converted in coordinate and converted not in current_player.marbles:
                if converted in [(c, d) for player in self.players for c, d in player.marbles]:
                    converted_next = vector.convert(*converted).indice
                    if converted_next in coordinate and converted_next in [(c, d) for player in self.players for c, d in player.marbles]:
                        converted_next_next = vector.convert(*converted_next).indice
                        index += 1
                        if converted_next_next in coordinate and converted_next_next in [(c, d) for player in self.players for c, d in player.marbles] or index == len(selected):
                            pass
                        else:
                            yield converted
                            if self.to_move == []:
                                self.to_move.append(converted)
                                self.to_move.append(converted_next)
                    else:
                        yield converted
                        if self.to_move == []:
                            self.to_move.append(converted)
                else:
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
        print(self.to_move)

    def move(
        self, current_player, new_coordinate, len, args:tuple=None, old_coordinate=None
    ):
        if len == 1 and new_coordinate in self.possibility(old_coordinate):
            current_player.marbles.remove(old_coordinate)
            current_player.marbles.append(new_coordinate)
            return True
        if len >= 2 and new_coordinate in self.can_move(*args):
            for i in self.neighbor(new_coordinate):
                if i in self.selected:
                    break
            old_coordinate = i
            vector = Vector2((new_coordinate[0] - old_coordinate[0], new_coordinate[1] - old_coordinate[1]))
            queue = []
            for i in self.to_move:
                converted = vector.convert(*i).indice
                for player in self.players:
                    if i in player.marbles and i not in current_player.marbles:
                        player.marbles.remove(i)
                        queue.append(i)
                        player.marbles.append(converted)
            for i in queue:
                self.to_move.remove(i)
            for i in self.selected:
                converted = vector.convert(*i).indice
                current_player.marbles.remove(i)
                current_player.marbles.append(converted)
                
            return True

        return False
    
    def loose(self, current_player):
        return not len(current_player.marbles)
