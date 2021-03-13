import pygame
from math import pi, sin, cos
from AbaLesExcepetions import AbaloneException


class CreateBoard:

    def __init__(self, size, radius, sides=6):
        assert not any(n for n in size if n == 0) or radius != 0, "Value is not valid"
        self.x, self.y = size
        self.radius = radius
        self.polygon_outline = None
        self.sides = sides

    def draw_regular_polygon(self, surface, color, outline=0):

        pygame.draw.polygon(surface, color,
                            [(self.x + self.radius * cos(2 * pi * i / self.sides),
                              self.y + self.radius * sin(2 * pi * i / self.sides))
                             for i
                             in
                             range(self.sides)], outline)

        self.polygon_outline = outline

    def draw_ceil(self, surface, color, outline=0):
        if self.polygon_outline is None:
            raise AbaloneException().missing_values("Please set polygon First")

        x = self.x
        list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
        radius_circle = self.radius / (pi * (self.sides/2))
        x = x // 2 + 40
        y = self.y // 2 - (self.polygon_outline + radius_circle)

        coordinates = []
        for i in list_coo_x:
            for p in range(i):
                coordinates.append((x + (p * radius_circle * outline), y))
            y += radius_circle
        
        for i in coordinates:
            pygame.draw.circle(surface, color, i, radius_circle, outline)
        coordinates.append(radius_circle)
        return coordinates
