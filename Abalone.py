import pygame
from math import pi, sin, cos
from AbaLesExcepetions import AbaloneException


class CreateBoard:

    def __init__(self, size, radius, sides=6):
        self.coordinates = []
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
        list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))

        radius_circle = self.radius / (pi * (self.sides / 2))

        x = round(self.x + self.radius * cos(2 * pi * 2 / self.sides)) + radius_circle - 6
        
        y = round(self.y + self.radius * sin(2 * pi * 4/ self.sides)) + radius_circle + 7
        sub = []
        
        for n, i in enumerate(list_coo_x):
            for p in range(i):
                sub.append((x + (p * radius_circle * outline), y))

                if len(sub) == i:
                    self.coordinates.append(sub)
                    sub = []
            x = x + radius_circle if n > 3 else x - radius_circle
            y = y + 2*radius_circle - 7
            

        sprites = [ pygame.draw.circle(surface, color, i, radius_circle, outline)for i in [i for c in self.coordinates for i in c]]
        
        return radius_circle,sprites






