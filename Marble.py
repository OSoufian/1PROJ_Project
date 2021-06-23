import pygame as pg
from pygame.constants import NOEVENT
from pygame.draw import circle
from vector import Vector2
from Team import Team

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
        to_move = []
        selected = sorted(self.selected)
        abs1, abs2, *abs3 = selected
        vector = Vector2((abs1[0] - abs2[0], abs1[1] - abs2[1]))
        players_marble = [(c, d) for player in self.players for c, d in player.marbles]
        converted = vector.convert(*abs1).indice
        for __ in range(2):
            if converted in coordinate and converted not in current_player.team.marbles:
                nearest_value, *_ = [i for i in self.neighbor(converted) if i in selected]
                if converted not in players_marble:
                    yield converted
                else:
                    a = [*self.can_push(converted, Vector2((converted[0] - nearest_value[0], converted[1] - nearest_value[1])), len(selected), current_player.team, coordinate, players_marble)]
                    if all(a) and len(selected) > len(a) + 1:
                        yield converted
            vector = -vector
            converted = vector.convert(*selected[-1]).indice

        mixx = self.neighbor(abs1) + self.neighbor(abs2) + (self.neighbor(*abs3) if abs3 else [])
        mix = [i for i in mixx if mixx.count(i) <= 1 and i not in players_marble]
        for i in mix:
            nearest_value, *_ = [i for i in self.neighbor(i) if i in selected]
            vector_2 = Vector2((i[0] - nearest_value[0], i[1] - nearest_value[1]))
            for j in selected:
                coordina = vector_2.convert(*j)
                if coordina.indice in players_marble:
                    break
            else:
                yield i

        yield to_move
        

    def move(
        self, current_player, new_coordinate, lenght, teams, args:tuple=None, old_coordinate=None
        ):
        if lenght == 1 and new_coordinate in self.possibility(old_coordinate):
            if old_coordinate in current_player.marbles:
                current_player.marbles.remove(old_coordinate)
                current_player.marbles.append(new_coordinate)
            else:
                for player in self.players:
                    if old_coordinate in player.marbles:
                        player.marbles.remove(old_coordinate)
                        player.marbles.append(new_coordinate)
            return True
        if lenght >= 2:
            *can_move, to_move = self.can_move(*args)

        if lenght >= 2 and new_coordinate in can_move:
            queue = []
            players_marble = [(c, d) for player in self.players for c, d in player.marbles]
            nearest_value, *_ = [i for i in self.neighbor(new_coordinate) if i in self.selected]
            vector = Vector2((new_coordinate[0] - nearest_value[0], new_coordinate[1] - nearest_value[1]))
            
            for i in range(1, lenght):
                case = (vector * i).convert(*nearest_value).indice
                if case not in args[0] or case not in players_marble:
                    break
                else:
                    queue.append(case)
            player_marble_copy = [player.marbles.copy() for player in self.players]
            for i in queue:
                converted = vector.convert(*i).indice
                for player, player_copy in zip(self.players, player_marble_copy):
                    if i in player_copy and i not in current_player.team.marbles:
                        player.marbles.remove(i)
                        if converted in args[0]:
                            player.marbles.append(converted)
                        else:
                            current_player.team.points += 1
                            win = self.win(current_player.team)
                            if win:
                                print("tiens tu as gagné :p", current_player.team)
            for i in self.selected:
                converted = vector.convert(*i).indice
                if i in current_player.marbles:
                    current_player.marbles.remove(i)
                    current_player.marbles.append(converted)
                else:
                    for player in self.players:
                        if i in player.marbles:
                            player.marbles.remove(i)
                            player.marbles.append(converted)
            for team in teams:
                team.update()
            return True
        return False
    
    def win(self, current_player):
        return current_player.team.team.points == 6

    def can_push(self, position, vector, lenght, current_player, coordinate, players_marbles):
        for i in range(1, lenght):
            case = (vector * i).convert(*position).indice
            if case in coordinate and case in players_marbles:
                yield case not in current_player.team.team.marbles
            else:
                return