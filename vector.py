class Vector2:

    def __init__(self, coordnates, lenght=1) -> None:
        x, y = coordnates
        self.x = x
        self.y = y
        self.lenght = lenght
    
    def convert(self, x, y):
        x = x + self.x
        y = y + self.y
        return Vector2((x, y), 1)
    
    def __eq__(self, vecteur) -> bool:
        return self.lenght == vecteur.lenght
    
    def __lt__(self, vecteur) -> bool:
        return self.lenght < vecteur.lenght
    
    def __str__(self):
        return f"Vector(x = {self.x}, y = {self.y}, lenght={self.lenght})"

    def __mul__(self, nbr):
        return Vector2((self.x * nbr, self.y * nbr), self.lenght)

if __name__ == "__main__":
    print(Vector2((0, 0), 1) > Vector2((-1, 0), 2))
