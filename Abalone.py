import pygame
from math import pi, sin, cos


class CreateBoard:

    def __init__(self, size, radius):
        self.coordinates = []
        assert not any(n for n in size if n == 0) or radius != 0, "Value is not valid"
        self.x, self.y = size
        self.radius = radius

    def draw_regular_polygon(self, surface, color, outline=0):    
        pygame.draw.polygon(surface, color, [(round(self.x + self.radius * cos(2 * pi * i / 6)), round(self.y + self.radius * sin(2 * pi * i / 6))) for i in range(6)], outline)


    def draw_ceil(self, surface, color, outline):
        list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
        radius_circle = self.radius / (pi * (6 / 2))
        x = round(self.x + self.radius * cos(2 * pi * 2 / 6)) + radius_circle - 6        
        y = round(self.y + self.radius * sin(2 * pi * 4/ 6)) + radius_circle + 7
        sub = []
        
        for n, i in enumerate(list_coo_x):            
            for p in range(i):
                sub.append((x + (p * radius_circle * outline), y))
                if len(sub) == i:
                    self.coordinates.append(sub)
                    sub = []

            x = x + radius_circle if n > 3 else x - radius_circle
            y = y + 2 * radius_circle - 7

        sprites = [ pygame.draw.circle(surface, color, i, radius_circle, outline)for i in [i for c in self.coordinates for i in c]]
        
        for center in [i for c in self.coordinates for i in c]:
            sprites.append(pygame.draw.circle(surface, color, center, radius_circle))
            pygame.draw.circle(surface, (180, 50, 0), center, radius_circle, 3)
            
        return radius_circle, sprites