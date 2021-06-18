import pygame as pg
from pygame.draw import circle


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

        if indice_y-1 < len(self.coordinates) and 0 <= indice_y-1:
            if indice_x < len(self.coordinates[indice_y-1]) and 0 <= indice_x:
                
                neighbor.append(self.coordinates[indice_y-1][indice_x])
                if indice_x == 0 and indice_y>4:
                    neighbor.append(self.coordinates[indice_y-1][indice_x+1])

            if indice_x-1 < len(self.coordinates[indice_y-1]) and 0 <= indice_x-1:
                neighbor.append(self.coordinates[indice_y-1][indice_x+1 if indice_y>4 else indice_x-1])
                
        if indice_y+1 < len(self.coordinates) and -1 < indice_y+1:
            if indice_x < len(self.coordinates[indice_y+1]) and 0 <= indice_x:
                neighbor.append(self.coordinates[indice_y+1][indice_x])
                
                if indice_x == 0 and indice_y<4:
                    neighbor.append(self.coordinates[indice_y+1][indice_x+1])

            if indice_x-1 < len(self.coordinates[indice_y+1]) and 0 <= indice_x-1:
                neighbor.append(self.coordinates[indice_y+1][indice_x+1 if indice_y<4 else indice_x-1])

        if indice_y < len(self.coordinates) and -1 < indice_y:
            if indice_x+1 < len(self.coordinates[indice_y]) and 0 <= indice_x+1:
                neighbor.append(self.coordinates[indice_y][indice_x+1])
            if indice_x-1 < len(self.coordinates[indice_y]) and -1 < indice_x-1:
                neighbor.append(self.coordinates[indice_y][indice_x-1])

        return neighbor
    
    def possibility(self, xy):
        coordinates = set([(round(c), round(d)) for player in self.players for c, d in player.marbles])
        deffault = set(tuple(map(round, (x, y))) for x, y in self.neighbor(xy))
        return tuple(deffault.difference(coordinates))

    def can_move(self, xy) -> bool:
        if not any(circle for player in self.players for circle in player.marbles if circle in self.neighbor(xy)):
            return True
        return False

    # def move(self, old_coordinate, new_coordinate):
    #     if self.can_move(old_coordinate, new_coordinate):
            

    def count(self, pieces, player):
        return sum(n for n in pieces[player])

    def win(self, pieces_left) -> bool:
        return pieces_left < 1

    # def remove_pieces(self, pieces) -> dict:
    #     raise