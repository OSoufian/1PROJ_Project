import pygame


class Marble:

    def __init__(self, surface, coordinates):
        self.coordinates = coordinates
        self.surface = surface
        self.clicked = []

    def draw_clickable(self, coordinate_ceil, color=(255, 255, 255)):
        assert coordinate_ceil in self.coordinates, "Coordiante ouside shape"

        pygame.draw.circle(self.surface, color, coordinate_ceil, coordinate_ceil[-1])

    def can_move(self, coordinate, new_coordinate) -> bool:
        raise Exception("Not implemented")

    def move(self, old_coordinate, new_coordinate):
        if self.can_move(old_coordinate, new_coordinate):
            pass
        raise Exception("Todo")

    def count(self, pieces, player):
        return sum(n for n in pieces[player])

    def win(self, pieces_left) -> bool:
        return pieces_left < 1

    def remove_pieces(self, pieces) -> dict:
        raise
       