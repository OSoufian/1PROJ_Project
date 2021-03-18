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
                            [(round(self.x + self.radius * cos(2 * pi * i / self.sides)),
                              round(self.y + self.radius * sin(2 * pi * i / self.sides)))
                             for i
                             in
                             range(self.sides)], outline)

        self.polygon_outline = outline

    def draw_ceil(self, surface, color, outline=0):
        if self.polygon_outline is None:
            raise AbaloneException().missing_values("Please set polygon First")

        x = self.x
        radius_circle = (self.radius//2)//5

        list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
        
        x = radius_circle*5
        y = radius_circle
        coordinates = []
        for i, n in enumerate(list_coo_x):
            for p in range(1,(n+1)):
                coordinates.append(((i+1)*p*radius_circle+x, (i+1)*radius_circle+y))
        # print(coordinates)
        
        for i in coordinates:
            pygame.draw.circle(surface, color, i, radius_circle, outline)
        coordinates.append(radius_circle)
        return coordinates
