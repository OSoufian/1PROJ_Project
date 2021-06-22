class Vector2:

    def __init__(self, coordnates, lenght=1) -> None:
        self.x, self.y = coordnates
        self.lenght = lenght
    
    def convert(self, x, y):
        return Vector2((x+self.x, y+self.y), 1)

    def __neg__(self):
        return Vector2((self.x * - 1, self.y * -1), self.lenght)
    
    def __eq__(self, vecteur) -> bool:
        return self.lenght == vecteur.lenght
    
    def __lt__(self, vecteur) -> bool:
        return self.lenght < vecteur.lenght
    
    def __str__(self):
        return f"Vector(x = {self.x}, y = {self.y}, lenght={self.lenght})"

    def __mul__(self, nbr):
        return Vector2((self.x * nbr, self.y * nbr), self.lenght)
    
    def __truediv__(self, nbr):
        return Vector2((self.x // nbr, self.y // nbr), self.lenght)
    
    def __neg__(self):
        return Vector2((self.x * -1, self.y * -1), self.lenght)

    def __truediv__(self, nbr):
        return Vector2((self.x // nbr, self.y // nbr), self.lenght)

    @property
    def indice(self):
        return (self.x, self.y)

if __name__ == "__main__":
    print(Vector2((0, 0), 1) > Vector2((-1, 0), 2))

